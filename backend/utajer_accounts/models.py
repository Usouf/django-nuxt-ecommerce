from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from helpers.models import BaseModel


class User(AbstractUser, BaseModel):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'

class UserAddress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

