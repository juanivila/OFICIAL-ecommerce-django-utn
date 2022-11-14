from django.urls import path

from . import views

app_name = 'contacto'

urlpatterns = [
	path('', views.Contacto.as_view(), name="contacto"),
	path('success-contacto/', views.SuccessContacto.as_view(), name="success-contacto"),
	
	]
