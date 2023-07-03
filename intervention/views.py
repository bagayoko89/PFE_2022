from django.shortcuts import render
from .forms import InterForm
from django.contrib import messages
from machine.models import Machine
from station.models import Station
from .models import Inter
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def inter(request,pk):
    if request.method =='POST':
        form= InterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = InterForm()

    return render(request, 'intervention/inter.html', locals())

#liste de validation
@login_required(login_url='login')
def list_inter(request, pk):
    inter=Inter.objects.all()
    context={'inter':inter,}
    return render(request, 'intervention/list_inter.html', context)

