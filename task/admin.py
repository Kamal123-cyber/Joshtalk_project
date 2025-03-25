from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_type', 'status', 'created_at', 'completed_at')
    list_filter = ('status', 'task_type', 'created_at', 'completed_at')
    search_fields = ('name', 'description', 'task_type')
    ordering = ('-created_at',)
    filter_horizontal = ('assigned_users',)  # For ManyToMany field in admin

admin.site.register(Task, TaskAdmin)
