from django.db import models
from .user import User

class Vuelo(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Piloto', on_delete=models.CASCADE)
    nombrePiloto = models.CharField('Nombre Piloto',max_length=50)
    origen = models.CharField('Origen',max_length=50)
    destino = models.CharField('Destino',max_length=50)
    fechaSalida = models.DateField('Fecha de Salida')
    fechaLlegada = models.DateField('Fecha de Llegada')
    horaSalida = models.TimeField('Hora de Salida')
    horaLlegada = models.TimeField('Hora de Llegada')
    cantidadPasajeros = models.IntegerField('Cantidad Pasajeros')
    