from django.shortcuts import render
from django.http import HttpResponse
from .models import Clase, Profesor
from django.urls import reverse_lazy
from django.views.generic import CreateView

def home_view(request):
    return render(request, "reserves/home.html")

def create_view(request, profesor, suplente, nivel, descripcion, estado):
    clase = Clase.objects.create(profesor = profesor, suplente = suplente , nivel = nivel, descripcion = descripcion, estado = estado)
    return HttpResponse(f"Las clases registradas fueron: <br> Profesor:{profesor} <br> Clase:{nivel} <br> Estado:{estado}")

def list_view(request):
    clases = Clase.objects.all().order_by('estado', 'suplente')
    contexto_dict = {'clases': clases}
    return render(request, "reserves/list.html", contexto_dict)

def detail_view(request, reserves_id):
    clases = Clase.objects.get(id=reserves_id)
    contexto_dict = {"clases": clases}
    return render(request, "reserves/detail.html", contexto_dict)

def filter_by_profesor(request, profesor_name):
    clases = Clase.objects.filter(profesor__nombre=profesor_name)
    contexto_dict = {'clases': clases}
    return render(request, "reserves/filtered_list.html", contexto_dict)

def filter_by_suplente(request, suplente_name):
    clases = Clase.objects.filter(suplente__nombre=suplente_name)
    contexto_dict = {'clases': clases}
    return render(request, "reserves/filtered_list.html", contexto_dict)


class ClaseCreateView(CreateView):
    model= Clase
    template_name = "reserves/clases/form_create_clases.html"
    fields = ['profesor', 'suplente', 'nivel', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
    success_url = reverse_lazy("reserves-list")

class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = "reserves/clases/form_create_profesor.html"
    fields = ['nombre']
    success_url = reverse_lazy("reserves-list")