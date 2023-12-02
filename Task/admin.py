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
    search_fields = ('title__startswith', )
    search_help_text = "notice : search task's title ."

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

    # add a summary of complete or not complete task
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        # Calculate the number of completed and not completed tasks
        completed_count = Task.objects.filter(completed=True).count()
        not_completed_count = Task.objects.filter(completed=False).count()

        # Add the counts to extra_context
        extra_context['completed_count'] = completed_count
        extra_context['not_completed_count'] = not_completed_count

        return super().changelist_view(request, extra_context=extra_context)

