from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import Creerutlisateur
from django.contrib import messages

# Create your views here.

def inscription(request):
    form=Creerutlisateur()
    if request.method=='POST':
        form=Creerutlisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request, 'compte/inscription.html', context)

def acces(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, "il y'a une erreur dans le nom d'utilisateur et/ou le mot de passe ")
    return render(request, 'compte/acces.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
