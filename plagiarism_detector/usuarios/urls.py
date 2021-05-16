from django.urls import path, include
from usuarios import views

urlpatterns = [
    
    path('signup/', views.SignUpView, name="signup"),
    path('profile/', views.profile_view, name="profile"),
    path('update_password/', views.update_password, name="update_password"),
    path('update_image/', views.update_image, name="update_image"),

]
