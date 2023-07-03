from django.shortcuts import render
from .models import Machine
from station.models import Station
from machine.forms.form_ajout import AjoutForm
from station.form.form_ajout import AjouForm
from problem.models import Prob
from problem.forms import Ajoutprob
from django.contrib import messages
from ishikawa.models import *
from whys.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
# Accueil
def home(request):
    return render(request, 'machine/acceuil.html')

# choix de la machine mode opérateur
@login_required(login_url='login')
def choix_machine(request):
    machine=Machine.objects.all()
    context={'machine':machine}
    return render(request, 'machine/Choix_machine.html', context)

# choix du suivi
@login_required(login_url='login')
def choix_suivi(request, pk):
    machine=Machine.objects.get(id=pk)
    context={'machine':machine}
    return render(request, 'machine/choix_suivi.html', context)

# vue d'accès aux options et l'affichage des diiférentes machines
@login_required(login_url='login')

def opt(request):
    machine = Machine.objects.all()
    stat = Station.objects.all
    context = {'machine': machine, 'stat':stat}
    return render(request, 'machine/mach.html', context)


# Ajouter une nouvelle station
@login_required(login_url='login')
def ajout_machine(request):
    if request.method =='POST':
        form= AjoutForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = AjoutForm()

    return render(request, 'machine/ajout_machine.html', locals())

# ajouter une nouvelle machine
@login_required(login_url='login')
def ajout_station(request):
    if request.method =='POST':
        form= AjouForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = AjouForm()

    return render(request, 'station/ajout_station.html', locals())

# ajouter un problème
@login_required(login_url='login')

def ajout_problem(request):
    if request.method =='POST':
        form= Ajoutprob(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = Ajoutprob()

    return render(request, 'problem/ajout_problem.html', locals())


@login_required(login_url='login')
def DOT(request, pk):
    return render(request, 'machine/DOT.html')

@login_required(login_url='login')
def RM(request):
    machine=Machine.objects.all()
    context={'machine':machine}
    return render(request, 'machine/RM_machine.html', context)

@login_required(login_url='login')
def RM_choix(request,pk):
    machine=Machine.objects.get(id=pk)
    prob=Prob.objects.all()
    context = {'prob': prob, 'machine':machine}
    return render(request, 'machine/liste_problem.html', context)

# Vue des 5M d'Ishikawa
@login_required(login_url='login')
def prob_suivi(request, pk,pt):
    machine = Machine.objects.get(id=pk)
    prob = Prob.objects.get(id_problem=pt)
    context={'prob':prob,'machine':machine}
    return render(request, 'machine/RM_choix.html', context)


@login_required(login_url='login')
def analyse(request, pk,pt,):
    machine=Machine.objects.get(id=pk)
    prob=Prob.objects.get(id_problem=pt)
    cmac = Cause_machine.objects.filter(cause=pt)
    cmat = Cause_matiere.objects.filter(cause=pt)
    cmi = Cause_milieu.objects.filter(cause=pt)
    cme = Cause_methode.objects.filter(cause=pt)
    cmai = Cause_main.objects.filter(cause=pt)
    if Macine==True:
        imac = Macine.objects.get(id_problem=pt)
        cmac = Cause_machine.objects.filter(cause=imac)
    if Matière==True:
        imat = Matière.objects.get(id_problem=pt)
        cmat = Cause_matiere.objects.filter(cause=imat)

    if Milieu==True:
        imi = Milieu.objects.get(id_problem=pt)
        cmi = Cause_milieu.objects.filter(cause=imi)

    if Méthode==True:
        ime = Méthode.objects.get(id_problem=pt)
        cme = Cause_methode.objects.filter(cause=ime)

    if Main_oeuvre==True:
        imai = Main_oeuvre.objects.get(id_problem=pt)
        cmai = Cause_main.objects.filter(cause=imai)
    context={'prob':prob,'cmac':cmac,'cmat':cmat,'cmi':cmi,'cme':cme, 'cmai':cmai, 'machine':machine}
    return render(request, 'ishikawa/analyse.html', context)

# Vues des 5Whys liés aux 5M

@login_required(login_url='login')
def why_mac(request, pk, pt, pr):
    cmac=Cause_machine.objects.get(id=pr)
    why=Why_mac.objects.filter(cons=cmac)
    context={'why':why, 'cmac':cmac,}
    return render(request, 'whys/whymac.html', context)

@login_required(login_url='login')
def why_mat(request, pk, pt, pr):
    cmat=Cause_matiere.objects.get(id=pr)
    why=Why_mat.objects.filter(cons=cmat)
    context={'why':why, 'cmac':cmat,}
    return render(request, 'whys/whymat.html', context)

@login_required(login_url='login')
def why_mil(request, pk, pt, pr):
    cmi=Cause_milieu.objects.get(id=pr)
    why=Why_mi.objects.filter(cons=cmi)
    context={'why':why, 'cmi':cmi,}
    return render(request, 'whys/whymil.html', context)

@login_required(login_url='login')
def why_met(request, pk, pt, pr):
    cme=Cause_methode.objects.get(id=pr)
    why=Why_me.objects.filter(cons=cme)
    context={'why':why, 'cme':cme}
    return render(request, 'whys/whyme.html', context)

@login_required(login_url='login')
def why_mai(request, pk, pt, pr):
    cmai=Cause_main.objects.get(id=pr)
    why=Why_mai.objects.filter(cons=cmai)
    context={'why':why, 'cmai':cmai}
    return render(request, 'whys/whymai.html', context)



# Partie process
@login_required(login_url='login')
def choix_process(request):
    machine=Machine.objects.all()
    context = {'machine': machine}
    return render(request, 'machine/choix_mac_process.html', context)
@login_required(login_url='login')
def suivi_proc(request,pk):
    machine=Machine.objects.get(id=pk)
    context = {'machine': machine}
    return render(request, 'machine/suivi_process.html', context)