import cmath
from distutils.command.upload import upload
from email.mime import image
from msilib import FCICreate
from pickle import TRUE
from tabnanny import verbose
from tkinter import FIRST
from django.db import models

from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural  = 'Habilidades Empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    JOB_CHOICES = {
        ('0', 'CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','VENTAS'),
        ('4','SEGURIDAD'),
        ('5','DIRECTOR EJECUTIVO'),
        ('6','DIRECTOR DE OPÉRACIONES'),
        ('7','DIRECTOR COMERCIAL'),
        ('8','DIRECTOR MARKETING'),
        ('9','DIRECTOR DE RECURSOS HUMANOS'),
        ('10','DIRECTOR FINANCIERO'),
        ('11','SISTEMA'),
        ('12','OTRO'),
    }
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres Completos', max_length=60, blank=TRUE)
    job = models.CharField('trabajo', max_length=20, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural   = 'Empleados de la empresa'
        ordering = ['-first_name','last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name


        