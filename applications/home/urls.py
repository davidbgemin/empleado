from unicodedata import name
from django.contrib import admin
from django.urls import path

# por cada vista creada (se importarán acá las vistas) se crea una url
from .views import PruebaView, PruebaListView, ListarPrueba, PruebaCreateView

urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista_prueba/', ListarPrueba.as_view()),
    path('add/', PruebaCreateView.as_view(), name='prueba_add'),
]