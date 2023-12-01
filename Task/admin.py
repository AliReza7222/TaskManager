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
    list_display = [
        'title',
        'due_date',
        'completed'
    ]
    list_filter = ['completed']
    sortable_by = ['due_date']
    actions = [
        'mark_to_completed',
        'mark_to_not_completed'
    ]

    # action for mark to completed task .
    def mark_to_completed(self, request, queryset):
        updated = queryset.update(completed=True)
        self.message_user(
            request, f'{updated} mark to completed task .'
        )

    # action for mark to not completed task
    def mark_to_not_completed(self, request, queryset):
        updated = queryset.update(completed=False)
        self.message_user(
            request, f'{updated} mark to not completed task .'
        )

    # short description view in admin panel
    mark_to_not_completed.short_description = 'mark task for not completion'
    mark_to_completed.short_description = 'mark task for completion'

