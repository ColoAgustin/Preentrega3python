from django.db import models

class Noticias(models.Model):
    news = models.CharField(max_length=40)
    
class Pilotos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)

class Fechas(models.Model):
    fecha = models.CharField(max_length=40)
    lugar = models.CharField(max_length=20)
    
