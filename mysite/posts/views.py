from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from .forms import UserRegisterForm

# Create your views here.

def index(request):
    return render(request, 'posts/home.html')



def online(request):
    return render(request, 'posts/online.html')


def register(request):
    if  request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'le Compte de {username} à été crée avec succès !')
            return redirect('/posts/')
    else:
        form = UserRegisterForm()
    return render(request, 'posts/register.html', {'form': form})