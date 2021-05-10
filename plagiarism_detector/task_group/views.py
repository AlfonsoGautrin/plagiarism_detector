from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        #essays = Essay.objects.all()
        #return render(request, 'index.html', {
        #    'essays': essays
        #})

        return render(request,'task_group_index.html')
    else:
        return redirect('login')
