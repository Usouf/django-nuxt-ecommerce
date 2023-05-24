from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models # User, Email, EmailVerification, UserAddress

@admin.register(models.User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']
    list_filter = ['username', 'email', 'first_name', 'last_name']
    list_editable = ['username']

@admin.register(models.Email)
class EmailAdmin(ImportExportModelAdmin):
    list_display = ['id', 'email',]
    list_filter = ['email']

@admin.register(models.EmailVerification)
class EmailVerificationAdmin(ImportExportModelAdmin):
    list_display = ['id', 'email']
