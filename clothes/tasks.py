from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_new_clothing_email(clothing_name):
    try:
        subject = f'New Clothing Added: {clothing_name}'
        message = f'The clothing item "{clothing_name}" has been successfully added to the site!'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['abbaszadeeyyub@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
        print(f"Email sent successfully for {clothing_name}!")

    except Exception as e:
        print(f"Error sending email for {clothing_name}: {e}")
