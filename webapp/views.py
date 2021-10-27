from django.shortcuts import render
from . models import Persona

def base(request):
    datos = Persona.objects.all()
    context = {'datos': datos}
    return render(request, 'webapp/base.html',context)

def index(request):
    datos = Persona.objects.all()
    context = {'datos': datos}
    return render(request, 'webapp/index.html',context)

def about(request):
    return render(request, 'webapp/about.html', {})    

def portfolio(request):
    return render(request, 'webapp/portfolio.html', {})    

def contacto(request):
    return render(request, 'webapp/contacto.html', {})    
