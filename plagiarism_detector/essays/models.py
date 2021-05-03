from django.db import models


# Create your models here.
class Essay(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=9000)
    author = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)


def getDateFormated(self):
    return self.date.strftime(' %d-%m-%Y')


