from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegisterUserView(CreateView):
    form_class= UserCreationForm
    template_name='contas/register.html'
    success_url = reverse_lazy('login')

class LoginUserView(LoginView):
    template_name='contas/login.html'

class LogoutUserView(LogoutView):
    next_page=reverse_lazy('login')