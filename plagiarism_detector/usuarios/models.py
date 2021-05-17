from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser#ALFONSO G: AbstractBaseUser es el padre de la clase usuario que incluye Django





class Usuario(AbstractUser) :

    image    = models.ImageField(upload_to = 'users_images',unique=False,)
    username = models.CharField(unique=True, default='Nombre', max_length=50)
    email    = models.EmailField(unique=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):

        return f'ID: {self.id} NOMBRE: {self.username} Correo: {self.email} Imagen: {self.image}'

   