from django.db import models
from usuarios.models import Usuario

# Create your models here.
class TaskGroup(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(null=True, blank=True)
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

