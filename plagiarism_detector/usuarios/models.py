from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager #ALFONSO G: AbstractBaseUser es el padre de la clase usuario que incluye Django

class Rol(models.Model) :
    nombre = models.CharField('nombre rol', max_length=20, unique=True)

    def __str__(self):

        return f'ID: {self.id} NOMBRE_ROL: {self.nombre}'

class UsuarioManager(BaseUserManager) :
    def create_user(self, correo, nombre, password = None) :
        if not correo :
            raise Value('Falta el correo')

        user = self.model(
            correo = self.normalize_email(correo),
            nombre = nombre
        )

        user.set_password(password)
        print(f'con: {user.password}')
        user.set_password(password)
        print(f'con: {user.password}')
        return user

    def create_superuser(self, correo, nombre, password) :
        user = self.create_user(
            correo,
            nombre = nombre,
            password = password
        )

        rolAdmin = Rol.objects.filter(nombre='ADMIN')[0]
        user.rol=rolAdmin
        user.save()
        return user




class Usuario(AbstractBaseUser) :
    correo  = models.EmailField('correo', unique=True)
    nombre  = models.CharField('nombre', max_length=100, unique=False)
    foto    = models.ImageField(unique=False)
    rol     = models.ForeignKey(Rol, on_delete = models.PROTECT)
    objects = UsuarioManager()

    USERNAME_FIELD = 'correo' #ALFONSO G: Campo que se usara para iniciar seccion
    REQUIRED_FIELDS = ['nombre']

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

    def __str__(self):
        super(Usuario, self).__init__()
        return f'ID: {self.id} NOMBRE: {self.nombre} CORREO: {self.correo}'
