# clothing/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Clothing

@shared_task
def send_clothing_added_email(clothing_id):
    try:
        clothing = Clothing.objects.get(pk=clothing_id)
        producer_email = clothing.producer.email #get producer email.
        subject = 'New Clothing Added'
        message = f'Your clothing item "{clothing.name}" has been added.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [producer_email]

        send_mail(subject, message, from_email, recipient_list)
        print(f"Email sent for clothing ID: {clothing_id}") # add logging.
    except Clothing.DoesNotExist:
        print(f"Clothing with ID {clothing_id} does not exist.") #add logging.
    except Exception as e:
        print(f"Error sending email: {e}") #add logging.