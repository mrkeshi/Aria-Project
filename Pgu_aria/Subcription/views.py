from datetime import timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from math import ceil
from workspace_module.models import Project, Task
from .models import PaymentSession, Subscription
from .serializers import SubscriptionSerializer,SubscriptionStatusSerializer
import requests
from django.utils import timezone

class StartPaymentAPIView(APIView):
    def post(self, request):
        plan = request.data.get('plan')
        amount_map = {
            "silver": 990000,
            "gold": 1990000
        }

        if plan not in amount_map:
            print(f"[Warning] درخواست پرداخت با پلن نامعتبر: {plan} توسط کاربر {request.user}")
            return Response({'error': 'پلن انتخاب شده معتبر نیست.'}, status=status.HTTP_400_BAD_REQUEST)

        amount = amount_map[plan]
        description = f"خرید اشتراک {plan} توسط {request.user.username}"
        callback_url = f"{settings.FRONTEND_BASE_URL}/dashboard/sub/verify?plan={plan}"

        data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,
            "amount": amount,
            "description": description,
            "callback_url": callback_url,
        }

        try:
            res = requests.post(
                "https://sandbox.zarinpal.com/pg/v4/payment/request.json",
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            response = res.json()
            print(f"[Info] پاسخ زرین پال استارت پرداخت برای کاربر {request.user}: {response}")
        except Exception as e:
            print(f"[Error] خطا در ارتباط با درگاه پرداخت برای کاربر {request.user}: {e}")
            return Response({'error': 'خطا در ارتباط با درگاه پرداخت.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if response.get('data', {}).get('code') == 100:
            authority = response['data']['authority']
            PaymentSession.objects.create(
                user=request.user,
                authority=authority,
                plan=plan,
                amount=amount
            )
            payment_url = f"https://sandbox.zarinpal.com/pg/StartPay/{authority}"
            print(f"[Info] جلسه پرداخت ایجاد شد برای کاربر {request.user} با authority: {authority}")
            return Response({'url': payment_url})

        print(f"[Warning] خطا در ایجاد پرداخت برای کاربر {request.user}: {response}")
        return Response({'error': 'خطا در ایجاد پرداخت.'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyPaymentAPIView(APIView):
    def get(self, request):
        authority = request.GET.get('authority')
        status_param = request.GET.get('status')
        plan = request.GET.get('plan')

        if not authority or not status_param or not plan:
            print(f"[Warning] پارامترهای ورودی ناقص در تایید پرداخت توسط کاربر {request.user}: {request.GET}")
            return Response({'error': 'پارامترهای ورودی ناقص هستند.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            print("------------")
            print(plan)
            print("\n \n -------------told ------")
            payment_session = PaymentSession.objects.get(
                authority=authority,
                user=request.user,
                plan=plan,
                is_verified=False
            )
            print("\n \n -------------bad ------")

            print(f"Verify payment: user={request.user}, authority={authority}, plan={plan}")

        except PaymentSession.DoesNotExist:
            print(f"[Warning] پرداخت یافت نشد یا قبلاً تأیید شده است برای کاربر {request.user} با authority: {authority}")
            return Response({'error': 'پرداخت یافت نشد یا قبلاً تأیید شده است.'}, status=status.HTTP_404_NOT_FOUND)

        if status_param != 'OK':
            print(f"[Info] پرداخت لغو یا ناموفق برای کاربر {request.user} با authority: {authority}")
            return Response({'error': 'پرداخت توسط کاربر لغو یا ناموفق بوده است.'}, status=status.HTTP_400_BAD_REQUEST)

        verify_data = {
            "merchant_id": settings.ZARINPAL_MERCHANT_ID,
            "amount": payment_session.amount,
            "authority": authority
        }

        try:
            res = requests.post(
                "https://sandbox.zarinpal.com/pg/v4/payment/verify.json",
                json=verify_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            response = res.json()
            print(f"[Info] پاسخ زرین پال وریفای پرداخت برای کاربر {request.user}: {response}")
        except Exception as e:
            print(f"[Error] خطا در ارتباط با درگاه پرداخت در وریفای برای کاربر {request.user}: {e}")
            return Response({'error': 'خطا در ارتباط با درگاه پرداخت.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if response.get('data', {}).get('code') in [100, 101]:
            ref_id = response['data'].get('ref_id')
            if not ref_id:
                print(f"[Error] کد پیگیری معتبر دریافت نشد در وریفای پرداخت برای کاربر {request.user}")
                return Response({'error': 'کد پیگیری معتبر دریافت نشد.'}, status=status.HTTP_400_BAD_REQUEST)

            plan_days = {
                "silver": 30,
                "gold": 30
            }.get(plan, 30)

            subscription, _ = Subscription.objects.get_or_create(user=request.user)
            subscription.activate_plan(
                new_plan=plan,
                new_plan_days=plan_days,
                new_plan_price=payment_session.amount,
                transaction_id=ref_id
            )

            payment_session.is_verified = True
            payment_session.save()

            serializer = SubscriptionSerializer(subscription)
            print(f"[Info] پرداخت با موفقیت تأیید شد برای کاربر {request.user} با ref_id: {ref_id}")
            return Response({
                'message': 'پرداخت با موفقیت تأیید شد.',
                'ref_id': ref_id,
                'subscription': serializer.data
            })

        print(f"[Warning] تأیید پرداخت ناموفق بود برای کاربر {request.user}: {response}")
        return Response({'error': 'تأیید پرداخت ناموفق بود.'}, status=status.HTTP_400_BAD_REQUEST)




class SubscriptionStatusView(APIView):

    def get(self, request):
        user = request.user

        try:
            sub = Subscription.objects.get(user=user)
            now = timezone.now()

            if sub.expires_at and sub.expires_at > now:
                delta = sub.expires_at - now
                remaining_days = ceil(delta.total_seconds() / 86400)
            else:
                remaining_days = 0

            is_active = sub.expires_at is None or sub.expires_at > now
            project = Project.objects.filter(id=user.current_project.id).first()

            plan = project.project_manager.subscription.plan
            manager_plan_active = project.project_manager.subscription.expires_at is None or project.project_manager.subscription.expires_at > now
            admin_projects = Project.objects.filter(project_manager=user)
            total_projects = admin_projects.count()
            total_tasks = Task.objects.filter(project__in=Project.objects.filter(project_manager=request.user)).count()
            user_ids = admin_projects.values_list("users", flat=True)
            total_users = len(set(user_ids))

            raw_limits = settings.SUBSCRIPTION_LIMITS.get(sub.plan, {})

            limits = {
                "max_projects": 9999 if sub.plan == "gold" else raw_limits.get("max_projects", 0),
                "max_tasks_per_project": 9999 if sub.plan == "gold" else raw_limits.get("max_tasks_per_project", 0),
                "max_users_per_project": 9999 if sub.plan == "gold" else raw_limits.get("max_users_per_project", 0),
            }

            data = {
                "plan": sub.plan,
                "started_at": sub.started_at,
                "expires_at": sub.expires_at,
                "is_active": is_active,
                "remaining_days": remaining_days,
                "total_projects": total_projects,
                "total_tasks": total_tasks,
                "total_users": total_users,
                "limits": limits,
                "manager_plan":plan,
                "manager_plan_active":manager_plan_active
            }
        except Subscription.DoesNotExist:
            project = Project.objects.filter(id=user.current_project.id).first()
            plan = project.project_manager.subscription.plan
            manager_plan_active = project.project_manager.subscription.expires_at is None or project.project_manager.subscription.expires_at > now
            data = {
                "plan": "free",
                "started_at": None,
                "expires_at": None,
                "is_active": False,
                "remaining_days": 0,
                "total_projects": 0,
                "total_tasks": 0,
                "total_users": 0,
                "limits": {
                    "max_projects": 1,
                    "max_tasks_per_project": 0,
                    "max_users_per_project": 0,
                },
                "manager_plan": plan,
                "manager_plan_active": manager_plan_active
            }

        serializer = SubscriptionStatusSerializer(data)
        return Response(serializer.data)