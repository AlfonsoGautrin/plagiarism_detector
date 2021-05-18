from django.db import models
from task_group.models import TaskGroup
from authors.models import Author
from usuarios.models import Usuario

# Create your models here.
class Essay(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=9000)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE, default=-1)
    date = models.DateField(null=True, blank=True)
    task_group = models.ForeignKey(TaskGroup, null=False, on_delete=models.CASCADE, default=-1)
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

def getDateFormated(self):
    return self.date.strftime(' %d-%m-%Y')

class EssayPlagiarism(models.Model) :
    essay1 = models.IntegerField(null=True)
    essay2 = models.IntegerField(null=True)
    task_group = models.ForeignKey(TaskGroup, null=False, on_delete=models.CASCADE, default=-1)
    plagiarism = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def get_plagiarism(self):
        return f'{self.plagiarism * 100}%' 

    def compute_jaccard(self):
        sentence1 = Essay.objects.get(id=self.essay1).content
        sentence2 = Essay.objects.get(id=self.essay2).content
        words_in_sentence1 = set(sentence1.split(" "))
        words_in_sentence2 = set(sentence2.split(" "))
        self.plagiarism = len(words_in_sentence1 & words_in_sentence2) / len(words_in_sentence1 | words_in_sentence2)   