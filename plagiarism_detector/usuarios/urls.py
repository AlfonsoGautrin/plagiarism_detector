from django.urls import path, include
from usuarios import views




urlpatterns = [
    
    path('signup/', views.SignUpView, name="signup")
]
