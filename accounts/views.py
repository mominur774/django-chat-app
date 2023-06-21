from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from accounts.forms import LoginForm, RegistrationForm
from django.contrib.auth import logout

# Create your views here.

class RegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = '/accounts/login/'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')