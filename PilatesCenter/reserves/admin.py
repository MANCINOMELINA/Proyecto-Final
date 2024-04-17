from django.contrib import admin
from .models import Profesor, Suplente, Estado, Clase

admin.site.register(Profesor)
admin.site.register(Suplente)
admin.site.register(Estado)
admin.site.register(Clase)