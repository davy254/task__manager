from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_due = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.task_name

