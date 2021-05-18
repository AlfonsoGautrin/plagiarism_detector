from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from .models import Author


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        authors = Author.objects.filter(user=request.user.id)
        return render(request, 'authors_index.html', {
            'authors': authors
        })
    else:
        return redirect('login')


def create(request):
    if request.user.is_authenticated :
        return render(request, 'authors_form.html', {
            'title': 'Crear Nuevo Autor',
            'index': -1
        })
    else :
        return redirect('login')


def edit(request, author_index: int):
    if request.user.is_authenticated :
        author = Author.objects.get(id=author_index)
        return render(request, 'authors_form.html', {
            'title': 'Editar Autor',
            'author': author,
            'index': author_index
        })
    else :
        return redirect('login')


def delete(request, author_index: int):
    if request.user.is_authenticated :
        instance = Author.objects.get(id=author_index)
        instance.delete()
        messages.success(request, 'Autor Eliminado Correctamente')
        return redirect('authors.index')
    else :
        return redirect('login')




def save(request):
    if request.user.is_authenticated :
        id = int(request.POST['author_id'])
        now = datetime.date.today()
        if id == -1:
            author = Author(
                name=request.POST['name'],
                created_at=now,
                user=request.user
            )
            author.save()
            messages.success(request, 'Autor Creado Correctamente')

        else:
            author = Author.objects.filter(id=id).first()
            author.name=request.POST['name']
            author.created_at=now
            author.save()
            messages.success(request, 'Autor Editado Correctamente')
           

        return redirect('authors.index')
    else :
        return redirect('login')

 