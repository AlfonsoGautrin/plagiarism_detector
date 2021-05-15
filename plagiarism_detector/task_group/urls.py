from django.urls import path
from task_group  import views

urlpatterns = [
    path('/', views.index, name='task_group.index'),
    path('/create/', views.create, name='task_group.create'),
    path('/edit/<int:group_index>', views.edit, name='task_group.edit'),
    path('/delete/<int:group_index>', views.delete, name='task_group.delete'),
    path('/save/', views.save, name='task_group.save')

]
