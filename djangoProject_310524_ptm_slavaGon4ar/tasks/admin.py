from django.contrib import admin
from .models import Task, SubTask, Category

# Регистрация модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'deadline')
    ordering = ('deadline',)

# Регистрация модели SubTask
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'task__title')
    list_filter = ('status', 'deadline')
    ordering = ('deadline',)

# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)