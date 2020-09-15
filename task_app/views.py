from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import  JSONParser
from .serializers import TaskSerializer
from . models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   UpdateModelMixin, RetrieveModelMixin,
                                   DestroyModelMixin)
from rest_framework.authentication import  SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def home(request):
    tasks = Task.objects.all().order_by('date_due')
    return render(request, 'task_app/home.html', {'tasks':tasks})

# function Based API views
"""
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return  Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = TaskSerializer(task, data=data)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)

"""

# class based API views
class TaskListAPIView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many= True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, id):
        task = self.get_object(id)
        task.delete()
        return  Response(status=status.HTTP_204_NOT_FOUND)

    def put(self, request, id):
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# using generic views
class GenericAPIView(GenericAPIView, ListModelMixin,
                     CreateModelMixin, UpdateModelMixin,
                     RetrieveModelMixin, DestroyModelMixin):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return  self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return  self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)
