# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
    SubTaskListCreateView, SubTaskRetrieveUpdateDestroyView,
    TaskStatisticsView, CategoryViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    # Задачи
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail-update-delete'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),

    # Подзадачи
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail-update-delete'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list-create'),
    path('', include(router.urls)),

]
