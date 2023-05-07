import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4 ,unique=True, editable=False)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def retrieve(self):
        self.deleted_at = None
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True