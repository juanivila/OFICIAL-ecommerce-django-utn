from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	# Inside each product
	fieldsets = [
		("Producto", {"fields": ['nombre_producto', 'tipo_de_prenda', 'color', 'talle']}),
		("Valores", {"fields": ['valor']}),
		("Stock", {"fields": ['stock']}),
		]
	
	# Table
	list_display = ['nombre_producto', 'tipo_de_prenda', 'color', 'talle', 'stocks']


admin.site.register(Valor)
