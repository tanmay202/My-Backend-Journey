from django.urls import path
from .import views 
from django.contrib.auth import views as loginView
urlpatterns = [
    path('register/',views.register),
    path('login/',loginView.LoginView.as_view(template_name='users/login.html')),
]