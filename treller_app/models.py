from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=99)
    description = models.TextField()
    status = models.CharField(max_length=99, choices=[('todo', 'To do'), ('inwork', 'In work'), ('completed', 'Completed')], default='todo')
    priority = models.CharField(max_length=99, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    tine_limit = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tasks')
    
    