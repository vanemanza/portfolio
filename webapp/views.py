from django.shortcuts import render, redirect
from . models import Persona
from proyectos.models import Proyecto
from contacto.forms import FormularioContacto
from django.core.mail import EmailMessage

def base(request):
    datos = Persona.objects.all()
    context = {'datos': datos}
    return render(request, 'webapp/base.html',context)

def index(request):
    datos = Persona.objects.all()
    context = {'datos': datos}
    return render(request, 'webapp/index.html',context)

def portfolio(request):
    datos = Persona.objects.all()
    proyectos = Proyecto.objects.all()
    contexto = {'proyectos': proyectos, 'datos': datos}
    return render(request, 'webapp/portfolio.html', contexto)    
   
def contacto(request):
    datos = Persona.objects.all()
    proyectos = Proyecto.objects.all()
    form = FormularioContacto()

    if request.method == 'POST':
        form = FormularioContacto(data=request.POST)
        if form.is_valid():
            nombre= request.POST.get("nombre")
            email= request.POST.get("email")
            contenido= request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App", "El usuario {} con la dirección {} escribe:\n\n{}".format(nombre, email, contenido), "", ["pruebasdev15@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")    
             
    return render(request, 'webapp/contacto.html', {'form': form, 'proyectos': proyectos, 'datos': datos})