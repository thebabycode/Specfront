from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse
from .models import Register
import json


def index(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            registermodel = Register.objects.all()
            #convert to list
            registermodeljson = list(registermodel.values())
            registermodeljson = registermodeljson[::-1]
            print(registermodeljson)
            return render(request, 'index.html', {'registermodeljson': registermodeljson})
    else:
        form = RegisterForm()
    return render(request, 'index.html', {'form': form})

def aimodel(request):
    
    return render(request, 'aimodel.html')

# Create your views here.
