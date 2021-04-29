from django.urls import path
from essays import views

urlpatterns = [
    path('/', views.index, name='essays.index'),
    # path('/create/', views.create, name='essays.create'),
    # path('/edit/<int:essay_index>', views.edit, name='essays.edit'),
    # path('/delete/<int:essay_index>', views.delete, name='essays.delete'),
    # path('/show/<int:essay_index>', views.show, name='essays.show'),
    # path('/save/', views.save, name='essays.save')
]
