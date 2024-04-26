from django import forms
from .models import Profesor, Clase, Avatar
from django.contrib.auth.models import User

class ClaseCreateForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['profesor', 'suplente', 'nivel', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
        labels = {
            'profesor': 'Seleccionar el profesor',
            'suplente': 'Seleccionar el suplente',
            'nivel': 'Seleccionar el nivel',
            'descripcion': 'Seleccionar el descripcion',
            'fecha_inicio': 'Seleccionar el fecha_inicio',
            'fecha_fin': 'Seleccionar el fecha_fin',
            'estado': 'Seleccionar el estado',
        }

class ProfesorCreateForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre']
        labels = {'profesor': 'Seleccionar el profesor'}
        

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']   
        
        
class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']             