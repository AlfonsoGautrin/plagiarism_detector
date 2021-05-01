from django.db import models
from django.contrib.auth.models import AbstractBaseUser #ALFONSO G: AbstractBaseUser es el padre de la clase usuario que incluye Django

class Rol(models.Model):
    nombre = models.CharField('nombre rol', max_length=20, unique=True)

    def __str__(self, arg):

        return f'ID: {self.id} NOMBRE_ROL: {self.nombre}'

class Usuario(AbstractBaseUser):
    nombre     = models.CharField('nombre', max_length=100, unique=False)
    correo     = models.EmailField()
    contrasena = models.CharField('contrasena', max_length=30, unique=False)
    foto       = models.ImageField('imagen', default = True, unique=False)
    rol        = models.ForeignKey(Rol, on_delete = models.PROTECT)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELD = ['nombre', 'correo', 'contrasena', 'rol']

    #ALFONSO G: Metodo sobre escrito para que los usuarios funcionen con el admin de Django
    def has_perm(self, perm, obj = None):
        return True

    #ALFONSO G: Para que el admin sepa donde buscar el modelo de los usuarios
    def has_module_perms(self, app_label):
        return True
    #ALFONSO G: Para que el admin identifique a los administadores
    @property
    def is_staff(self):
        return True if self.rol == 1 else False

    def __str__(self, arg):
        super(Usuario, self).__init__()
        return f'ID: {self.id} NOMBRE: {self.nombre} CORREO: {self.correo}'
