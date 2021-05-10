from django.urls import path
from task_group  import views

urlpatterns = [
    path('/', views.index, name='task_group.index'),

]
