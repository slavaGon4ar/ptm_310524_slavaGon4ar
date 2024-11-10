from rest_framework import generics, filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.db.models import Count, Q
from .models import Task, SubTask,  Category
from .serializers import TaskCreateSerializer, SubTaskCreateSerializer, CategoryCreateSerializer


# Представление для списка задач и создания задачи
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


# Представление для получения, обновления и удаления задачи
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


# Представление для списка подзадач и создания подзадачи
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all().order_by('-created_at')
    serializer_class = SubTaskCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


# Представление для получения, обновления и удаления подзадачи
class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer


# Агрегирующий эндпойнт для статистики задач (оставлен без изменений)
class TaskStatisticsView(APIView):
    def get(self, request):
        total_tasks = Task.objects.count()
        tasks_by_status = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(), status__in=['New', 'In progress']).count()

        data = {
            'total_tasks': total_tasks,
            'tasks_by_status': tasks_by_status,
            'overdue_tasks': overdue_tasks
        }
        return Response(data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        """
        Кастомный метод для подсчета количества задач в каждой категории.
        """
        category = self.get_object()
        task_count = Task.objects.filter(categories=category).count()
        return Response({'category_id': category.id, 'task_count': task_count})