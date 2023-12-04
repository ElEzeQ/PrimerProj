from django.db import models

# Create your models here. Tablas de la base de datos

class Jugadores(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    imagen = models.URLField(help_text="Cargar solo la url")
    describcion = models.TextField(help_text="Describcion breve del jugador")

    class Meta:
        ordering = ['nombre']