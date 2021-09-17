from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class resourceRestaurante(resources.ModelResource):
    class Meta:
        model = restaurante

class adminRestaurante(ImportExportModelAdmin, admin.ModelAdmin):
    search_files = ['nombre']
    list_display = ['nombre','telefono', 'direccion']
    resource_class = resourceRestaurante

admin.site.register(restaurante, adminRestaurante)

class resourcePlatillos(resources.ModelResource):
    class Meta:
        model = platillos

class adminPlatillos(ImportExportModelAdmin, admin.ModelAdmin):
    search_files = ['nombre']
    list_display = ['nombre','descripcion', 'precio']
    resource_class = resourcePlatillos

admin.site.register(platillos, adminPlatillos)