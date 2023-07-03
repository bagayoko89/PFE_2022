from django.shortcuts import render
from .forms import MicroForms
from django.contrib import messages
from machine.models import Machine
from station.models import Station
from .models import Micro
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def micro(request,pk):
    if request.method =='POST':
        form= MicroForms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = MicroForms()

    return render(request, 'micro_arrets/micro.html', locals())

#liste de down time
@login_required(login_url='login')
def list_micro(request, pk):
    micro=Micro.objects.all()
    context={'micro':micro}
    return render(request, 'micro_arrets/list_micro.html', context)




