from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from usuarios.models import Usuario

# Create your views here.
def SignUpView(request):
    if request.method == 'POST' :
        email      = request.POST['email']
        username   = request.POST['username']
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        password1  = request.POST['password1']
        password2  = request.POST['password2']

        email      = email.lower()
        first_name = first_name.capitalize()
        last_name  = capitalize_last_name(last_name)

        if not check_passwords(password1, password2) :
            error_message = 'Las contraseñas no coinciden'
            return send_error_message(error_message, email, username, first_name, last_name, request)

        if  email_exist(email) :
            error_message = 'Ya existe una cuenta con la direccion de correo ingresada'
            return send_error_message(error_message, email, username, first_name, last_name, request)
            

        elif  username_exist(username) :
            error_message = 'Ya existe una cuenta con ese nombre de usuario'
            return send_error_message(error_message, email, username, first_name, last_name, request)
        
        elif check_space_empty(username) :
            error_message = 'El nombre de usuario no puede contener espacios'
            return send_error_message(error_message, email, username, first_name, last_name, request)
        
        
        Usuario.objects.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password1,
            is_superuser=False
        )
        return redirect('login')
    return render(request, 'registration/signup.html', {'error':False})


def check_passwords(password1, password2) :
    return password1 == password2

def email_exist(value) :
    user = Usuario.objects.filter(email=value)
    if len(user) > 0:
        return True;
    return False;

def username_exist(value) :
    user = Usuario.objects.filter(username=value)
    if len(user) > 0:
        return True;
    return False;

def check_space_empty(word) :
    words_list = word.split() #ALFONSO G El metodo split crea una lista con cada palabra de un str
    return len(words_list) > 1 #Si la lista solo contiene mas de una palabra significa que el str contiene espacios

def capitalize_last_name(last_name) :
    last_names = last_name.split()
    last_name = ''
    for i in range(len(last_names)) :
        last_names[i] = last_names[i].capitalize()
        last_name += (last_names[i].capitalize() + ' ')
    return last_name
    



def send_error_message(error_message, email, username, first_name, last_name, request) :
    data = {
        'email'         : email,
        'username'      : username,
        'first_name'    : first_name ,
        'last_name'     : last_name,
        'error'         : True,
        'error_message' : error_message,  
    }
    return render(request, 'registration/signup.html', data)