from django.conf import settings
from django.core.mail import send_mail

def send_email(subject,message,to_email):
    to_emails = to_email if isinstance(to_email, list) else [to_email]

    # if isinstance(to_emails, list):
    #     to_emails = to_email
    # else:
    #     to_emails = [to_email, ]

    send_mail(subject,message,settings.EMAIL_HOST_USER,[to_email])