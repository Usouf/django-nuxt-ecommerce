import random

from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from helpers.models import BaseModel
from helpers.adapters import EmailAdapter


class User(AbstractUser, BaseModel):
    # username, firstname, lastname, email, is_staff, is_active, date_joined, password, last_login, is_active

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'

class Email(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emails')
    email = models.EmailField(max_length=254, unique=True)

    verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')
        db_table = 'emails'

    def send_otp(self):
        verification = EmailVerification.create(self)
        verification.send()
        return verification

    def __str__(self):
        return self.email

class EmailVerification(BaseModel):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name='verifications')
    otp = models.CharField(max_length=6)

    sent = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _('Email Verification')
        verbose_name_plural = _('Email Verifications')
        db_table = 'email_verifications'

    @classmethod
    def create(cls, email):
        otp = random.randint(100000, 999999)
        return cls._default_manager.create(email=email, otp=otp)

    def key_expired(self):
        return self.sent + timedelta(mins=10) <= timezone.now()

    def verify(self):
        if not self.key_expired() and not self.email.verified:
            email = self.email
            email.verified = True
            email.save()
            return email

    def send(self):
        ctx = {
            "email": self.email.email,
            "user": self.email.user,
            "otp": self.otp,
        }

        email_template = "helpers/account/email/email_verification"

        adapter = EmailAdapter()
        adapter.send_mail(email_template, [self.email.email], context=ctx)
        self.sent = timezone.now()
        self.save()

    def __str__(self):
        return "confirmation for %s" % self.email

class UserAddress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('User Address')
        verbose_name_plural = _('User Addresses')
        db_table = 'user_addresses'

    def __str__(self):
        return self.user.email + ' - ' + self.address + ' - ' + self.city + ' - ' + self.state + ' - ' + self.zip_code + ' - ' + self.phone_number + ' - ' + str(self.is_default)

