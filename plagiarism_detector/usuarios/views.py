from .forms import UserCreationFormWithEmail
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class registro(CreateView) :
    form_class    = UserCreationFormWithEmail
    success_url   = reverse_lazy('login')
    template_name = 'registration/register.html'

    