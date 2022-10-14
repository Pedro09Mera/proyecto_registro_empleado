from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from aplications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm

# Create your views here.


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'
    

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data['Departamento'],
            shor_name=form.cleaned_data['Shorname']
        )
        depa.save()

        nombre = form.cleaned_data['Nombre']
        apellido = form.cleaned_data['Apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '10',
            departamento=depa,
     
        )
        return super(NewDepartamentoView, self).form_valid(form)