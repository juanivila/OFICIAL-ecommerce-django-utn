from django.contrib import admin

from .models import Consulta, Respuesta


class RespuestaInline(admin.TabularInline):
	model = Respuesta
	extra = 0
	fields = ('respuesta',)


class ConsultaAdmin(admin.ModelAdmin):
	inlines = (RespuestaInline,)
	list_display = ('email', 'mensaje', 'fecha', 'respondido')
	list_filter = ('respondido', 'fecha')
	readonly_fields = ('email', 'mensaje', 'fecha', 'respondido')


admin.site.register(Consulta, ConsultaAdmin)
