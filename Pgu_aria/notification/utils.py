import requests
from django.conf import settings

def send_onesignal_notification(onesignal_user_id, heading, message, url=None):

    headers = {
        "Authorization": f"Basic {settings.ONESIGNAL_REST_API_KEY}",
        "Content-Type": "application/json; charset=utf-8",
    }

    payload = {
        "app_id": settings.ONESIGNAL_APP_ID,
        "include_external_user_ids": [onesignal_user_id],
        "headings": {"en": heading, "fa": heading},
        "contents": {"en": message, "fa": message},
    }
    if url:
        payload["url"] = url

    response = requests.post("https://onesignal.com/api/v1/notifications", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
