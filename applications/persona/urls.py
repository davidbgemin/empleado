
# !* parte introductoria del curso:
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('persona/', admin.site.urls),
# ]

# !* parte de vistas genéricas (sección 8):
from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import ListAllEmpleados,ListByAreaEmpleado, ListEmpleadosByKeyWord, ListHabilidadesEmpleado, EmpleadoDetailView, EmpleadoCreateView, SuccessView, EmpleadoUpdateView, EmpleadoDeleteView, InicioView, ListaEmpleadosAdmin

app_name = 'persona_app'

urlpatterns = [
    # !* urls de ListView:
    path('listar-todo-empleados/', ListAllEmpleados.as_view(), name='empleados_all'),
    path('lista-por-area/<shortname>/', ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('lista-empleados-admin/', ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('buscar-empleado-kword/', ListEmpleadosByKeyWord.as_view()),
    path('lista-habilidades-empleado/', ListHabilidadesEmpleado.as_view()),

    # !* urls de DetailView:
    path('ver-empleado/<pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),

    # !* urls de CreateView:
    path('crear-empleado/', EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', SuccessView.as_view(), name='correcto'),

    # !* urls de UpdateView:
    path('update-empleado/<pk>/', EmpleadoUpdateView.as_view(), name='modificar_empleado'),

    # !* urls de UpdateView:
    path('delete-empleado/<pk>/', EmpleadoDeleteView.as_view(), name='eliminar_empleado'),

    # !* urls de UpdateView:
    path('', InicioView.as_view(), name='inicio'),
]
