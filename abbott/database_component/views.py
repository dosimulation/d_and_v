from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    return render(request, 'index.html')

def transportation(request):
    return render(request, 'transportation.html')

def diabetes(request):
    return render(request, 'diabetes.html')

def nutrition(request):
    return render(request, 'nutrition.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def login_submit_view(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request, 'login.html', {
        'error_message': "Failed to authenticate.",
    })

def logout_view(request):
    logout(request)
    return redirect('/login/')