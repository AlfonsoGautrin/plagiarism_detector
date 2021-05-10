from django.db import models

# Create your models here.
class TaskGroup(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(null=True, blank=True)

