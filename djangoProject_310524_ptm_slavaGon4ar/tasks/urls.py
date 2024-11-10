# tasks/urls.py
from django.urls import path
from .views import TaskCreateView, TaskListView, TaskStatisticsView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),

]
