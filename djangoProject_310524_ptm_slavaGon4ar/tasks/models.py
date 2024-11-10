from django.db import models

class Category(models.Model):
    # Модель категории для задач
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Task(models.Model):
    # Варианты выбора для статуса задачи
    NEW = 'New'
    IN_PROGRESS = 'In progress'
    PENDING = 'Pending'
    BLOCKED = 'Blocked'
    DONE = 'Done'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (PENDING, 'Pending'),
        (BLOCKED, 'Blocked'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=200, unique=True, verbose_name="Название задачи")
    description = models.TextField(blank=True, null=True, verbose_name="Описание задачи")
    categories = models.ManyToManyField(Category, related_name="tasks", verbose_name="Категории")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW, verbose_name="Статус")
    deadline = models.DateTimeField(verbose_name="Дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

class SubTask(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название подзадачи")
    description = models.TextField(blank=True, null=True, verbose_name="Описание подзадачи")
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE, verbose_name="Основная задача")
    status = models.CharField(max_length=20, choices=Task.STATUS_CHOICES, default=Task.NEW, verbose_name="Статус")
    deadline = models.DateTimeField(verbose_name="Дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title