from rest_framework import  serializers
from .models import Task
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_name', 'date_created', 'date_due', 'description']
