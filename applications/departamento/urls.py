from tkinter import NE
from django.contrib import admin
from django.urls import path
from .views import NewDepartamentoView, DepartamentoListView

# para validar si funciona la url (importar la función en urlpatterns)
# def DesdeApp(self):
    # print('......corriendo url desde la app departamento.....')

app_name = 'departamento_app'

urlpatterns = [
    # path('departamento/', DesdeApp),
    # path('departamento/', admin.site.urls),
    path('new-departamento/', NewDepartamentoView.as_view(), name='nuevo_departamento'),

    path('departamento-lista/', DepartamentoListView.as_view(), name='departamento_list'),
]