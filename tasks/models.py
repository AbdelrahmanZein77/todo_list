from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_in = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True, null=True, blank=True)
    property = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    complated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
