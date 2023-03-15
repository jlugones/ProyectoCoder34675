from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
#def guardar_curso(request, camada):
#    curso = Curso(nombre="Pyhton", camada=23800)
#    curso.save()
#    return HttpResponse("usuario creado exitosamente")

def curso(request):
    return render(request, "base.html")

def estudiante(request):
    return render(request, "base.html")

def profesor(request):
    return render(request, "base.html")



