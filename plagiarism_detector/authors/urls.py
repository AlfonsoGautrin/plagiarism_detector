from django.urls import path
from authors import views

urlpatterns = [
    path('/', views.index, name='authors.index'),
    path('/create/', views.create, name='authors.create'),
    path('/edit/<int:author_index>', views.edit, name='authors.edit'),
    path('/delete/<int:author_index>', views.delete, name='authors.delete'),
    path('/save/', views.save, name='authors.save')

]
