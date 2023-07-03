from django.shortcuts import render
from .forms import DTForm
from django.contrib import messages
from machine.models import Machine
from .models import Down
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')

def DT(request,pk):
    if request.method =='POST':
        form= DTForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Données Stockées')

    else:
        form = DTForm()

    return render(request, 'down_time/DT.html', locals())

#liste de down time
@login_required(login_url='login')
def list_DT(request, pk):
    down=Down.objects.all()
    context={'down':down}
    return render(request, 'down_time/list_DT.html', context)


