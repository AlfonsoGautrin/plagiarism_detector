from django.db import models
from django.contrib.auth.models import AbstractUser#ALFONSO G: AbstractBaseUser es el padre de la clase usuario que incluye Django

class Rol(models.Model) :
    nombre = models.CharField('nombre rol', max_length=20, unique=True)

    def __str__(self):

        return f'ID: {self.id} NOMBRE_ROL: {self.nombre}'



class Usuario(AbstractUser) :

    foto     = models.ImageField(unique=False)
    username = models.CharField(unique=True, default='Nombre', max_length=50)
    email    = models.EmailField(unique=True)
    rol      = models.ForeignKey(Rol, on_delete = models.PROTECT, default=2)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    


