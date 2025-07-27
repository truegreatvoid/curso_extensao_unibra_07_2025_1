from django.db import models


class TaskStatus(models.TextChoices):
    TODO = 'todo', 'A Fazer'
    DOING = 'doing', 'Fazendo'
    DONE = 'done', 'Concluído'
