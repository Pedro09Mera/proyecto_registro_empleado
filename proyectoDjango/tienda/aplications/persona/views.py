from cgi import print_form
from dataclasses import dataclass
from multiprocessing.heap import Arena
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)
from aplications import departamento

from aplications.departamento.models import Departamento
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

class InicioView(TemplateView):
    """ Vista que carga la pagina de inico """
    template_name = 'inicio.html'
    

class ListAllEmpleados(ListView):
    template_name = 'persona/lista_all.html'
    paginate_by = 3
    ordering = 'first_name'
    #model = Empleado
    context_object_name = 'listaa'

    def get_queryset(self):
        #print('**********')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
            #first_name=palabra_clave
        )
        return lista

class ListByAreaempleado(ListView):
    #Lista de empleados de una are
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista


class ListaEmpleadoAdmin(ListView):
    #Lista de empleados de una are
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

class listEmpleadosBykword(ListView):
    template_name = 'persona/by_world.html'
    #paginate_by = 4
    #ordering = ''
    context_object_name = 'Empleados'

    def get_queryset(self):
        print('**********')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class LisHabilidadesEmpleados(ListView):
    template_name= 'persona/habilidades.html'
    context_object_name = 'Habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=4)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwarg):
        context = super(EmpleadoDetailView, self).get_context_data(**kwarg)
        context['Titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name 
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)      


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post (self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model =Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')
