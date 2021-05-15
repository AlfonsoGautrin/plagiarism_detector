from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from .models import TaskGroup


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        groups = TaskGroup.objects.all()
        return render(request, 'task_group_index.html', {
            'groups': groups
        })
    else:
        return redirect('login')


def create(request):
    if request.user.is_authenticated :
        return render(request, 'task_group_form.html', {
            'title': 'Crear Grupo de Tarea',
            'index': -1
        })
    else :
        return redirect('login')


def edit(request, group_index: int):
    if request.user.is_authenticated :
        group = TaskGroup.objects.get(id=group_index)
        return render(request, 'task_group_form.html', {
            'title': 'Editar Grupo de',
            'group': group,
            'index': group_index
        })
    else :
        return redirect('login')


def delete(request, group_index: int):
    if request.user.is_authenticated :
        instance = TaskGroup.objects.get(id=group_index)
        instance.delete()
        messages.success(request, 'Grupo de Tarea Eliminado Correctamente')
        return redirect('task_group.index')
    else :
        return redirect('login')




def save(request):
    if request.user.is_authenticated :
        id = int(request.POST['group_id'])
        now = datetime.date.today()
        if id == -1:
            task_group = TaskGroup(
                name=request.POST['name'],
                created_at=now,
            )
            task_group.save()
            messages.success(request, 'Grupo de Tarea Creado Creada Correctamente')

        else:
            print(request.POST['name'])
            task_group = TaskGroup.objects.get(id=id)
            print(task_group)
            task_group.name = request.POST['name'],
            task_group.created_at = now
            task_group.save()
            print(task_group)
            messages.success(request, 'Grupo de Tarea Editado Correctamente')

        return redirect('task_group.index')
    else :
        return redirect('login')

