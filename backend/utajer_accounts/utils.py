from .models import Email


def complete_signup(user):
    email = Email.objects.create(user=user, email=user.email)
    email.send_otp()
