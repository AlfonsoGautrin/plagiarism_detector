from django.db import models
from task_group.models import TaskGroup


# Create your models here.
class Essay(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=9000)
    author = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    task_group = models.ForeignKey(TaskGroup, null=False, on_delete=models.PROTECT, default=-1)


def getDateFormated(self):
    return self.date.strftime(' %d-%m-%Y')


class EssayPlagiarism(models.Model) :
    essays   = models.ManyToManyField(Essay)
    essayAVG = models.DecimalField(max_digits=100, decimal_places=2)
    date     = models.DateField()