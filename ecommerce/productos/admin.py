from django.contrib import admin
from .models import *


# Register your models here.
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
