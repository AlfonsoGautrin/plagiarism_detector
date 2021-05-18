from django.shortcuts import render, redirect
from django.contrib import messages
from essays.models import Essay
from task_group.models import TaskGroup
from authors.models import Author

# Create your views here.

def index(request):
    if request.user.is_authenticated:

        rows = []
        essays = Essay.objects.filter(user=request.user.id)
        task_groups = TaskGroup.objects.filter(user=request.user.id)
        authors = Author.objects.filter(user=request.user.id)
        groups = TaskGroup.objects.filter(user=request.user.id).order_by('created_at')[0:4]
        for group in groups:
            group_essays = Essay.objects.filter(task_group=group.id)
             
            rows.append({
                'name':group.name,
                'len':len(group_essays),
                'avg': (len(group_essays) * 100) / len(essays) if len(essays) != 0 else 0,
            })
           

        return render(request, 'dashboard_index.html', {
            'title':'Tablero Detección de Plagio',
            'essay_len': len(essays),
            'task_groups_len': len(task_groups),
            'author_len':len(authors),
            'rows':rows,
            'rows_len':len(rows)
        })
    else:
        return redirect('login')