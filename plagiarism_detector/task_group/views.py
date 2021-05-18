from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from .models import TaskGroup
from essays.models import EssayPlagiarism,Essay


# Create your views here.

def index(request):
    if request.user.is_authenticated:
       
        rows = []
        groups = TaskGroup.objects.all()

        for group in groups:
            essays = Essay.objects.filter(task_group=group.id)
            rows.append({
                'id':group.id,
                'name': group.name,
                'essays_size': len(essays),
                'created_at': group.created_at
            })
        return render(request, 'task_group_index.html', {
            'rows': rows
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
            'title': 'Editar Grupo de Tareas',
            'group': group,
            'index': group_index
        })
    else :
        return redirect('login')


def delete(request, group_index: int):
    if request.user.is_authenticated :
        instance = TaskGroup.objects.get(id=group_index)
        EssayPlagiarism.objects.filter(task_group=group_index).delete()
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
            task_group = TaskGroup.objects.filter(id=id).first()
            task_group.name=request.POST['name']
            task_group.created_at=now
            task_group.save()
            messages.success(request, 'Grupo de Tarea Editado Correctamente')
        return redirect('task_group.index')
    else :
        return redirect('login')

def verify(request,group_index: int):
    task_group = TaskGroup.objects.filter(id=group_index).first()
    essays = Essay.objects.filter(task_group=group_index)
    now = datetime.date.today()

    combinations = []
    for essay in essays:
        for essay2 in essays:
            if essay.id != essay2.id:
                combination = f'{essay.id}{essay2.id}'
                if not combination in combinations:
                    plagiarism = EssayPlagiarism(
                        essay1=essay.id,
                        essay2=essay2.id,
                        task_group=task_group,
                        
                    )
                    plagiarism.compute_jaccard()
                    plagiarism.save()
                    
                    combination = combination[::-1]
                    combinations.append(combination)
    
    results = []
    essay_plagiarisms = EssayPlagiarism.objects.filter(task_group=group_index)
    for essay_plagiarism in essay_plagiarisms:
        essay1 = Essay.objects.get(id=essay_plagiarism.essay1)
        essay2 = Essay.objects.get(id=essay_plagiarism.essay2)
        results.append({
            'id': essay_plagiarism.id,
            'essay1_id' :essay1.id,
            'essay1_name': essay1.title,
            'essay1_author':essay1.author.name,
            'essay2_id' :essay2.id,
            'essay2_name': essay2.title,
            'essay2_author':essay2.author.name,
            'avg': essay_plagiarism.get_plagiarism,
            'verified_on' : essay_plagiarism.date
        })

    return render(request, 'palgiarism.html', {
        'title': f'Palgio en grupo de tarea: {task_group.name}',
        'results': results,
    })
