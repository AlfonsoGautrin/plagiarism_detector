from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from .models import Essay,TaskGroup


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        essays = Essay.objects.all()
        return render(request, 'index.html', {
            'essays': essays
        })
    else:
        return redirect('login')


def create(request):
    if request.user.is_authenticated :
        task_groups = TaskGroup.objects.all()
        return render(request, 'form.html', {
            'title': 'Crear Ensayo',
            'task_groups': task_groups,
            'index': -1
        })
    else :
        return redirect('login')


def edit(request, essay_index: int):
    if request.user.is_authenticated :
        essay = Essay.objects.get(id=essay_index)
        task_groups = TaskGroup.objects.all()
        return render(request, 'form.html', {
            'title': 'Editar Ensayo',
            'essay': essay,
            'task_groups': task_groups,
            'index': essay_index
        })
    else :
        return redirect('login')


def delete(request, essay_index: int):
    if request.user.is_authenticated :
        instance = Essay.objects.get(id=essay_index)
        instance.delete()
        messages.success(request, 'Ensayo Eliminado Correctamente')
        return redirect('essays.index')
    else :
        return redirect('login')


def show(request, essay_index: int):
    if request.user.is_authenticated :
        instance = Essay.objects.get(id=essay_index)
        return render(request, 'show.html', {
            'title': 'Detalle de Ensayo',
            'essay': instance,
            'index': essay_index
        })
    else :
        return redirect('login')


def save(request):
    if request.user.is_authenticated :
        id = int(request.POST['essay_id'])
        now = datetime.date.today()
        if id == -1:

            essay = Essay(
                title=request.POST['title'],
                author=request.POST['author'],
                content=request.POST['content'],
                date=now
            )

            essay.save()
            messages.success(request, 'Ensayo Creado Correctamente')

        else:
            essay = Essay.objects.filter(id=id).first()
            essay.title = request.POST['title'],
            essay.author = request.POST['author'],
            essay.content = request.POST['content'],
            essay.date = now
            essay.save()
            messages.success(request, 'Ensayo Editado Correctamente')

        return redirect('essays.index')
    else :
        return redirect('login')
