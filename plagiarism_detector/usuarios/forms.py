from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm) : 
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres maximo ")

class Meta:
    model = User
    fields = ("email", "username", "password1", "password2")