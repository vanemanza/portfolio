from django.shortcuts import render
from . models import Vanesa

def base(request):
    datos = Vanesa.objects.all()
    context = {'datos': datos}
    return render(request, 'webapp/base.html',context)

def index(request):
    datos = Vanesa.objects.all()
    context = {'datos': datos}
    return render(request, 'webapp/index.html',context)
