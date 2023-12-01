from django.contrib import admin

from .models import Task


# registered the Task model to admin panel and created a custom admin panel
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'description',
        'due_date',
        'completed'
    ]
    list_display = ['title', 'due_date', 'completed']
    list_filter = ['completed']
    sortable_by = ['due_date']
