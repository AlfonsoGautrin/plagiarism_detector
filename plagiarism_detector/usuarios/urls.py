from django.urls import path, include
from usuarios import views



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
 
    path('registro/', views.registro.as_view(), name = 'registro')
]
