from django.db import models
from datetime import datetime

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"


class Suplente(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"


class Estado(models.Model):
    estado = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.estado}"


class Clase(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE,related_name='clases')
    suplente = models.ForeignKey(Suplente, on_delete=models.CASCADE,related_name='clases')
    nivel = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(default=datetime.now)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,related_name='clases')

    def __str__(self):
        return f"Se resgistró la clase {self.nivel} para el profesor {self.profesor}"

    def diferencia_año(self):
        mes_clase_fin = self.fecha_fin.month
        mes_clase_inicio = self.fecha_inicio.month
        diferencia = mes_clase_fin - mes_clase_inicio
        return diferencia