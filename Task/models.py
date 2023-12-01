from django.db import models

from .validators import check_text


class Task(models.Model):
    title = models.CharField(unique=True, validators=[check_text], max_length=150,
                             help_text='Your title should contain words, numbers and _ and start with words.')
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField()

    def __str__(self):
        return f'[{self.title}]-[{self.due_date}]-[{self.completed}]'
