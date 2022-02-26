from pyexpat import model
import re
from statistics import mode
from tkinter import Entry
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from django.urls import reverse_lazy

# forms:
from .forms import EmpleadoForm


# Create your views here.

# !******* 1. ListView (general) ******
# 1. listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all_empleados.html' # crear el template
    paginate_by = 4 # muestra 4 empleados por página, para cambiar a la siguiente página agregar al final de la url: ?page=2
    # ordering = 'first_name' # muestra los empleados ordenados alfabéticamente por el nombre
    ordering = 'id'
    context_object_name = 'empleados' # nombre del objeto que se va a mostrar en el template

    def get_queryset(self):
        # print('********************')
        palabra_clave = self.request.GET.get("kword","") # proviene del id del input
        lista = Empleado.objects.filter(
            # first_name proviene de los campos del modelo empleado:
            first_name__icontains= palabra_clave
        )
        # print('lista resultado: ', lista)
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado




# 2. listar todos los empleados que pertenecen a una área de la empresa
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_all_per_department.html'
    # en este ejemplo no se usará el context_object_name, en lugar de ello se usará el object_list directo en el html. Se puede omitir el context_object_name y agregar de frente object_list en el html pero es buena práctica usar el context_object_name
    context_object_name = 'empleados'

    def get_queryset(self):
        # en la url se agregará /shortname y filtará al dar enter
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            # tabla__campo
            departamento__shortname = area
        )
        return lista



# 3. listar los empleados por palabra clave
class ListEmpleadosByKeyWord(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        # print('********************')
        palabra_clave = self.request.GET.get("kword","") # proviene del id del input
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado: ', lista)
        return lista



# 4. listar habilidades de un empleadoº
# relación many to many
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # se obtendrá la lista de habilidades del empleado de id=4, si se cambia el id por el 1 mostrará las habilidades del empleado 1
        empleado = Empleado.objects.get(id=4)
        return empleado.habilidades.all()



# !******* 1. DetailView (general) ******
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    # sobreescribiendo el método get_context_data
    def get_context_data(self, **kwars):
        context = super(EmpleadoDetailView, self).get_context_data(**kwars)
        context['titulo'] = 'Empleado del mes'

        return context


# !******* 2. CreateView ******
class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    # para invocar a todos los campos de la tabla:
    # fields = '__all__'
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar'] # se comentan los fields ya que se usará EmpleadoForm
    form_class = EmpleadoForm
    
    # después de crear el empleado se redirige a la lista de empleados:
    # success_url = '/listar-todo-empleados/'

    # después de crear el empleado se redirige a la visa SuccessView (usando reverse_lazy):
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # lógica del proceso
        # crear la instancia sin guardar con commit=False
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # guardando en la base de datos
        empleado.save()
        print(empleado)
        return super(EmpleadoCreateView, self).form_valid(form)


# !******* 3. UpdateView ******
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST.get('first_name'))
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        # lógica del proceso:
        return super(EmpleadoUpdateView, self).form_valid(form)


# !******* 4. DeleteView ******
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')



# !* ******* Esquema de carpeta Templates ******
class InicioView(TemplateView):
    """vista que carga la página de inicio"""
    template_name = "inicio.html"