import uuid

from django.db import models
from django.db.models import Q
from django.utils import timezone


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
    )

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['created_at'], name='idx_timestamp_created'),
        ]


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        db_index=True,
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def soft_delete(self, user):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(
            update_fields=[
                'is_deleted',
                'deleted_at',
            ]
        )

    class Meta:
        abstract = True
        indexes = [
            models.Index(
                name='idx_not_deleted',
                fields=['deleted_at'],
                condition=Q(is_deleted=False),
            ),
            models.Index(
                name='idx_not_del_and_delat',
                fields=[
                    'is_deleted',
                    'deleted_at',
                ],
            ),
        ]


class BaseModel(
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        default=True,
        db_index=True,
    )

    class Meta:
        abstract = True
        indexes = [
            models.Index(
                fields=[
                    'name',
                    'created_at',
                    'active',
                ],
                name='idx_name_created_active',
            ),
        ]


class EmailMixin(models.Model):
    email = models.EmailField(
        'email address',
        unique=True,
        db_index=True,
    )

    class Meta:
        abstract = True
