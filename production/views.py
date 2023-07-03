from django.shortcuts import render, redirect
from .forms import ProdForm
from django.contrib import messages
from machine.views import choix_suivi
from machine.models import Machine
from .models import Prod
from .filters import Prodfilter
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def prod(request,pk):
    if request.method =='POST':
        form= ProdForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.id_machine=Machine(pk)
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = ProdForm()

    return render(request, 'production/prod.html', locals())

#liste de production
@login_required(login_url='login')
def list_prod(request, pk):
    prod=Prod.objects.filter(id_machine=pk)
    myfilter=Prodfilter(request.GET, queryset=prod)
    prod=myfilter.qs
    context={'prod':prod, 'myfilter':myfilter}
    return render(request, 'production/liste_prod.html', context)

@login_required(login_url='login')
def graphe(request, pk):
    pro=Prod.objects.filter(id_machine=pk)
    myfilter = Prodfilter(request.GET, queryset=pro)
    pro = myfilter.qs
    context={
        "pro":pro, 'myfilter':myfilter
    }
    return render(request, 'production/dashboard.html', context)

