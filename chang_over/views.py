from django.shortcuts import render
from .forms import ChangeForms
from django.contrib import messages
from machine.models import Machine
from .models import Change
from station.models import Station
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def chang(request,pk):
    if request.method =='POST':
        form= ChangeForms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = ChangeForms()

    return render(request, 'chang_over/chang.html', locals())

#liste de down time
@login_required(login_url='login')
def list_chang(request, pk):
    stat=Station.objects.filter(id_machine=pk)
    chang=Change.objects.all()
    context={'chang':chang, 'stat':stat}
    return render(request, 'chang_over/list_chang.html', context)



