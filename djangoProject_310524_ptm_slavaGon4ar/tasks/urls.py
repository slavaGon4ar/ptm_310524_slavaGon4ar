# tasks/urls.py
from django.urls import path
from .views import (
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
    SubTaskListCreateView, SubTaskRetrieveUpdateDestroyView,
    TaskStatisticsView
)

urlpatterns = [
    # Задачи
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail-update-delete'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),

    # Подзадачи
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail-update-delete'),

]
