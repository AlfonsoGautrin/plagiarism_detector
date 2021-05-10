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

        url = 'registration/signup.html'

        if not check_passwords(password1, password2) :
            error_message = 'Las contraseñas no coinciden'
            return send_error_message(error_message, email, username, first_name, last_name, request, url)

        if  email_exist(email) :
            error_message = 'Ya existe una cuenta con la direccion de correo ingresada'
            return send_error_message(error_message, email, username, first_name, last_name, request, url)
            

        elif  username_exist(username) :
            error_message = 'Ya existe una cuenta con ese nombre de usuario'
            return send_error_message(error_message, email, username, first_name, last_name, request, url)
        
        elif check_space_empty(username) :
            error_message = 'El nombre de usuario no puede contener espacios'
            return send_error_message(error_message, email, username, first_name, last_name, request, url)
        
        
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
    

def send_error_message(error_message, email, username, first_name, last_name, request,  url) :
    data = {
        'email'         : email,
        'username'      : username,
        'first_name'    : first_name ,
        'last_name'     : last_name,
        'error'         : True,
        'error_message' : error_message,  
    }
    return render(request, url, data)







""" def update_user(request) :
    user_id      = request.POST['user_id']
    email        = request.POST['email']
    username     = request.POST['username']
    first_name   = request.POST['first_name']
    lase_name   = request.POST['laste_name']

    email = email.lower()
    
    if email_exist(email) :
    
    elif check_space_empty(username) :

    elif username_exist(username) :

    user = Usuario.objects.filter(id=user.id)
    user.email=email.lower()
    user.username=username
    user.first_name=first_name.capitalize()
    user.last_name= capitalize_last_name(last_name) """

""" 
def add_image(request) :
    image = request.FILES """


""" def update_password(request) :
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if not check_passwords(password1, password2) :
        error = 'Las contraseñas no coinciden'
    
    user_id = request.POST['user_id']

    user = Usuario.objects.filter(id=user_id)

    user.password=Usuario.set_password(self, password1)
    user.save
    return """