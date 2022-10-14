from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba2

class IndexView(TemplateView):
   template_name = 'home/prueba.html'

class ResumenFoundationView(TemplateView):
   template_name = 'home/resumen.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['A','B','C','D']
    context_object_name = 'listaprueba'
    

class ModeloPruebaListView(ListView):
    model = Prueba2
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba2
    fields = ['titulo','subtitulo','cantidad']
    success_url = '/'
