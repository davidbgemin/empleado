from pyexpat import model
from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba

from .forms import PruebaForm

# Create your views here.
# !* 1. TemplateView
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


# !* 2. ListView
class PruebaListView(ListView):
    template_name = 'home/lista.html'
    # context_object_name será lo que se agregará en el html interpolado para que se muestre en la página
    context_object_name = 'listaNumeros'
    # model = MODEL_NAME (listview pide un model name, pero en este caso como no tenemos modelos de bases de datos, usaremos queryset). El arreglo aparecerá pintado en el html
    queryset = [0,10,20,30]

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html' # nombre del template
    model = Prueba # viene del modelo
    context_object_name = 'lista' # para el html


# !* 3. CreateView
class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = '/'