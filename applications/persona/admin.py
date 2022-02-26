from encodings import search_function
from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
# !* registrando el modelo Habilidades para que aparezca en el PA
admin.site.register(Habilidades)

# !* configurando el PA (la tabla empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    # para que aparezca en el PA con formato de tabla los siguientes campos de la tabla Empleado
    list_display = (
        # 'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    # función para que aparezca una nueva columna (que no está en la bd) en el PA de django con dos campos fusionados: first_name + last_name
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    # para que aparezca una barra de búsqueda según el first_name en la parte superior
    search_fields = ('first_name',)

    # para que aparezca al lado derecho una sección de filtro según el job y habilidades
    list_filter = ('job', 'habilidades',)

    # filtro horizontal para los campos: muchos a muchos:
    filter_horizontal = ('habilidades',)

# !* registrando el modelo Empleado 
admin.site.register(Empleado, EmpleadoAdmin)

