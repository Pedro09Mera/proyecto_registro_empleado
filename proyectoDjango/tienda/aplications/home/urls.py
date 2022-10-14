#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add-prueba/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path('resumen-fundation/', views.ResumenFoundationView.as_view(), name='resumen_fundation'),
]

