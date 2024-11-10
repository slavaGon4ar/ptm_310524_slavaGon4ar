# tasks/urls.py
from django.urls import path
from .views import TaskCreateView, TaskListView, TaskStatisticsView, SubTaskListCreateView, SubTaskDetailUpdateDeleteView

urlpatterns = [
    # Задачи
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),

    # Подзадачи
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),

]
