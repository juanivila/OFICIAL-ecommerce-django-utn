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
	
	# Customize
	list_display = ['nombre_producto', 'tipo_de_prenda', 'color', 'talle', 'stocks']
	list_filter = ('tipo_de_prenda', 'talle', 'color')
	search_fields = ('tipo_de_prenda', 'color')


admin.site.register(Valor)
