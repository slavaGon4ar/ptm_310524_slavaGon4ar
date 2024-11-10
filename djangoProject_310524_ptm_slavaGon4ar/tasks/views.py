# from django.shortcuts import render
#
# # Create your views here.
# # tasks/views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Task
# from .serializers import TaskSerializer
#
# class TaskCreateView(APIView):
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

# Эндпойнт для создания новой задачи
class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Эндпойнт для получения списка задач с фильтрацией и пагинацией
class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'deadline']

    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')

# Эндпойнт для получения статистики задач
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
