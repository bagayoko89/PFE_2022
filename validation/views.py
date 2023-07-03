from django.shortcuts import render
from .forms import ValForm
from django.contrib import messages
from machine.models import Machine
from .models import Val
from down_time.models import Down
from intervention.models import Inter
from chang_over.models import Change
from station.models import Station
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def val(request,pk):
    if request.method =='POST':
        form= ValForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.id_machine=Machine(pk)
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = ValForm()

    return render(request, 'validation/vali.html', locals())

#liste de validation
@login_required(login_url='login')
def list_val(request, pk):
    val=Val.objects.filter(id_machine=pk)
    context={'val':val}
    return render(request, 'validation/list_val.html', context)

@login_required(login_url='login')
def graphe(request, pk):
    val=Val.objects.filter(id_machine=pk)
    stat=Station.objects.filter(id_machine=pk)
    dt=Down.objects.filter(id_station=stat)
    inter = Inter.objects.filter(id_station=stat)
    chang = Change.objects.filter(id_station=stat)

    context={
        'val':val, 'stat':stat, 'dt':dt, 'inter':inter, 'chang':chang,
    }

    return render(request, 'validation/dashboard.html', context)
