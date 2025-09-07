from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_in = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True, null=True, blank=True)
    property = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    complated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def CreateToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)