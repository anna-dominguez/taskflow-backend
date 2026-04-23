from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_tasks_count')
    search_fields = ('name',)
    ordering = ('name',)

    def get_tasks_count(self, obj):
        return obj.tasks.count()
    get_tasks_count.short_description = 'Nombre de tâches'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description_short', 'is_completed', 'category', 'created_at')
    list_filter = ('is_completed', 'category', 'created_at')
    search_fields = ('description',)
    ordering = ('-created_at',)
    list_editable = ('is_completed',)

    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'
