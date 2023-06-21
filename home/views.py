from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    context = {
        'users': User.objects.exclude(username=request.user)
    }
    return render(request, 'home/index.html', context)