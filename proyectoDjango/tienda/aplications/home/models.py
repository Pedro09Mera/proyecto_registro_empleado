from django.db import models

class Prueba2(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)

