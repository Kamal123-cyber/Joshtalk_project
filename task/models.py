import uuid
from django.db import models
from useraccount.models import UserAccount  # Import UserAccount model

class TimeStampModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(TimeStampModel):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=50)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(UserAccount, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.name
