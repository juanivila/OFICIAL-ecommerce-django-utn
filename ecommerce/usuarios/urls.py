from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
	path('mis-datos/', views.mis_datos, name='mis-datos')
	]
