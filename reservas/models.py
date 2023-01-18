from django.db import models

# Create your models here.

personas = []

for i in range(1,16):
    #x =  'Seleccione cantidad de personas' if i == 0 else i
    personas.append((i,i))

class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    fono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad = models.IntegerField(choices=personas)
    estado = models.CharField(max_length=50, default='Disponible')
    observacion = models.TextField(null=True, blank=True)