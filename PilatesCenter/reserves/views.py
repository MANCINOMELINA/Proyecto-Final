from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Clase, Profesor
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserEditForm
from .models import Avatar
from .forms import AvatarCreateForm




def home_view(request):
    return render(request, "reserves/home.html")

@login_required
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


class ClaseCreateView(LoginRequiredMixin, CreateView):
    model= Clase
    template_name = "reserves/clases/form_create_clases.html"
    fields = ['profesor', 'suplente', 'nivel', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
    success_url = reverse_lazy("reserves-list")

class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    template_name = "reserves/clases/form_create_profesor.html"
    fields = ['nombre']
    success_url = reverse_lazy("reserves-list")
    

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "reserves/login.html", {"loguear": form})


def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "reserves/crear_usuario.html", {"crear": form})


def user_logout_view(request):
    logout(request)
    return redirect("login")    
    
      
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "reserves/user_edit_form.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user   
    
    
def avatar_view(request):
    if request.method == "GET":
        contexto = {"imagen": AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"imagen": form}


    return render(request, "reserves/avatar_create.html", context=contexto)    
    
    