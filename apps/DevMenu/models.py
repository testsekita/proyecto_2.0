from django.db import models

# Create your models here.
class restaurante(models.Model):
    pk_restaurante = models.AutoField(primary_key=True, null=False, blank=False)
    dueño = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=70, null=False, blank=False)

class platillos(models.Model):
    pk_platillo = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=35, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    imagen = models.URLField(max_length=8000, blank=False, null=False, default='https://i.pinimg.com/originals/e7/ee/13/e7ee13eacea7dea62f085b59b240b0b0.png')


