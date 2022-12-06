from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Inside each product
    fieldsets = [
        ("Producto", {"fields": ['nombre_producto', 'tipo_de_prenda', 'color', 'talle', 'genero']}),
        ("Valores", {"fields": ['valor']}),
        ("Stock", {"fields": ['stock']}),
        ("Imagen", {"fields": ['imagen']}),
    ]

    # Customize
    list_display = ['nombre_producto', 'genero', 'tipo_de_prenda', 'color', 'talle', 'stocks']
    list_filter = ('tipo_de_prenda', 'talle', 'color')
    search_fields = ('tipo_de_prenda', 'color')
    actions = ['eliminar_stock', 'exportar_a_json', 'ver_productos']

    @admin.action(description='Eliminar stock')
    def eliminar_stock(self, request, queryset):
        registro = queryset.update(stock=0)

        if registro == 1:
            self.message_user(request, f"{registro} producto actualizado.")
        if registro > 1:
            self.message_user(request, f"{registro} productos actualizados.")

    @admin.action(description='Exportar a JSON')
    def exportar_a_json(self, request, queryset):
        response = HttpResponse(content_type='application/json')
        serializers.serialize('json', queryset, stream=response)
        return response

    @admin.action(description='Ver productos')
    def ver_productos(self, request, queryset):
        ctx = {'productos': Producto.objects.all()}

        return render(request, 'admin/productos/productos.html', ctx)
