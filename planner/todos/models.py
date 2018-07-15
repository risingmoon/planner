from django.conf import settings
from django.db import models


class Todo (models.Model):
    DEFAULT = ''
    COMPLETED = 'CMP'
    STATUS_CHOICES = (
        (DEFAULT, 'default'),
        (COMPLETED, 'completed'))
    text = models.TextField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES)
    added = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(null=True)
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
