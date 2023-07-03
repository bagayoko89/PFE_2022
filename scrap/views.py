from django.shortcuts import render
from .forms import Scrapform
from django.contrib import messages
from machine.models import Machine
from .models import Scrap
from .filters import Scrapfilter
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def scrap(request,pk):
    if request.method =='POST':
        form= Scrapform(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = Scrapform()

    return render(request, 'scrap/scrap.html', locals())

#liste de down time
@login_required(login_url='login')
def list_scrap(request, pk):
    scrap=Scrap.objects.all()
    context={'scrap':scrap}
    return render(request, 'scrap/liste_scrap.html', context)

@login_required(login_url='login')

def graphe(request, pk):
    scrap=Scrap.objects.all()
    myfilter = Scrapfilter(request.GET, queryset=scrap)
    scrap = myfilter.qs
    context={'scrap':scrap, 'myfilter':myfilter}
    return render(request, 'scrap/dashboard_scrap.html', context)




