from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    apellidos = forms.CharField(label='Apellidos', max_length=50)
    departamento = forms.CharField(label='Departamento', max_length=50)
    shortname = forms.CharField(label='Shortname', max_length=50)