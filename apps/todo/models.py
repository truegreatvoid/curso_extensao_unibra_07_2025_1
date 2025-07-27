from django.db import models

from apps.core.constants import TaskStatus
from apps.core.models import BaseModel
from apps.customers.models import User


class Task(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
        db_index=True,
    )
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return f'{self.name} - {self.status}'
