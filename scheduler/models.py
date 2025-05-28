from django.db import models
import uuid
from enum import Enum


class TaskStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    COMPLETED = "COMPLETED", "Completed"

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length = 20,
        choices = TaskStatus.choices,
        default = TaskStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} [{self.status}]"
    
    
class TaskDependency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, related_name='dependent_task', on_delete=models.CASCADE)
    depends_on = models.ForeignKey(Task, related_name='prerequisite_tasks', on_delete=models.CASCADE)
    
    class meta:
        unique_together = ('task', 'depends_on')
        
    def __str__(self):
        return f"{self.task.name} depends on {self.depends_on.name}"
        
