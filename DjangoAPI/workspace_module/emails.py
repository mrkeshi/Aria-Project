from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def send_invitation_email(inviter_email, to_email, project, project_id, level, skill,islogin):
  if level ==2:
    level = 'کارمند ارشد'
  elif level == 3:
    level = 'کارمند عادی'
  else:
    return Response({'message': 'سطح کاریر یه درستی وارد نشده'}, status=status.HTTP_400_BAD_REQUEST)
  from_email = settings.EMAIL_HOST_USER
  subject = f'دعوت به همکاری در پروژه {project}'
  html_message = render_to_string('invite_email/invite_email.html',{'inviter_email':inviter_email, 'project':project, 'subject':subject, 'project_id':project_id, 'to_email':to_email, 'level':level, 'skill':skill,'islogin':islogin})
  plain_message = strip_tags(html_message)
  
  send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


def send_task_creation_email(task):
    if not settings.SEND_TASK_CREATION_EMAIL:
        return

    subject = f"تسک جدید: {task.title}"
    message = f"""
    سلام کاربر عزیز،

    یک تسک جدید با موضوع "{task.title}" در پروژه "{task.project.title}" برای شما تعریف شده است.

    لطفاً برای مشاهده تسک وارد سامانه شوید.
    """

    recipient_email = task.assigned.email
    if recipient_email:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False
        )
