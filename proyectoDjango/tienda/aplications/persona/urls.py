#from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
      path(
        '', 
        views.InicioView.as_view(),  
        name='inicio de nuetsra pagina'
         ),
    path(
        'listar-todo_empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
         ),
    path('lista_area/<shorname>/',
     views.ListByAreaempleado.as_view(),
         name='empleados_area'
         ),
    path('lista-empleados-admin/',
     views.ListaEmpleadoAdmin.as_view(),
         name='empleados_admin'
         ),
    path('buscar_empleado/', views.listEmpleadosBykword.as_view()),
    path('lista-habilidades-empleados/', views.LisHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
        ),
    path('add-empleado/',
          views.EmpleadoCreateView.as_view(),
          name='empleado_add'
          ),
    path(
        'success/', 
        views.SuccessView.as_view(),  
        name='correcto'
        ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),  
        name='modificar-empleado'
        ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),  
        name='eliminar-empleado'
        ),

]

