from django.urls import path
from . import views
from .views import TaskListAPIView, TaskDetailAPIView, GenericAPIView



urlpatterns = [
    # to use these paths un comment the function view
    path('', views.home , name='home'),
   # path('task-list', views.TaskAPIView),
    #path('detail/<int:pk>/', views.TaskAPIView),

    #using clas based views
    path('tasks-list-api/', TaskListAPIView.as_view() ),
    path('tasks-detail-api/<int:id>/', TaskDetailAPIView.as_view() ),

    # using generic views
    path('tasks-generic-api/', GenericAPIView.as_view()),
    path('tasks-generic-api/<int:pk>/', GenericAPIView.as_view()),

]