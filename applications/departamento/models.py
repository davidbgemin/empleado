from mailbox import mbox
from tabnanny import verbose
from django.db import models

# Create your models here.
class Departamento(models.Model):
    """Modelo para la tabla departamento"""
    name = models.CharField('Nombre', max_length=50, blank=True,) # editable=False,
    # blank permite que el campo no sea obligatorio, si se omite colocar blank el campo será obligatorio
    # editable=False --> hace que el campo no aparezca en el PA de django, es decir no se puede editar desde el PA, por defecto su valor es True
    shortname = models.CharField('Nombre corto', max_length=20, unique=True) # unique hace que el shortname sea único (no se repita)
    anulate = models.BooleanField('Anulado', default=False)

    # !* Configurando el PA
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Departamentos de la empresa'
        ordering = ['-name',] # ordena alfabéticamente por name en forma descendente
        unique_together = ('name', 'shortname') # unique together hace que no se repita 2 líneas que tengan name y shortname juntos

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.shortname

    