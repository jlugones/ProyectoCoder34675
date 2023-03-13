from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombres="Pyhton", camada=23800)
    curso.save()
    return HttpResponse("usuario creado exitosamente")

