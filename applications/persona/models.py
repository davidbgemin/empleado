from distutils.command.upload import upload
from hashlib import md5
from pyexpat import model
from tabnanny import verbose
from django.db import models
from applications.departamento.models import Departamento
# !* CKEditor:
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad


class Empleado(models.Model):
    """Modelo para la tabla empleado"""
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True, null=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    # !* FOREIGN KEY:
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # campo de imagen: se debe instalar pip install pillow
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # un empleado puede tener muchas habilidades, una habilidad puede se adquirida por varios empleados (relación de muchos a muchos)
    habilidades = models.ManyToManyField(Habilidades)
    # !* usando ckeditor: se agregó este campo después de la instalación de ckeditor (video 37)
    hoja_vida = RichTextField()

    # !* Configurando el PA
    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'last_name')


    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name