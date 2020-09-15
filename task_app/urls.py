from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('task-list', views.task_list),
    path('detail/<int:pk>/', views.task_detail)
]
