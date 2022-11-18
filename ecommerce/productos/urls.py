from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
	path('', views.home, name="home"),
	path('login/', views.login_page, name="login"),
	path('register/', views.register, name="register"),
	path('hombres/', views.hombres, name="categoria-hombres"),
	path('mujeres/', views.mujeres, name="categoria-mujeres"),
	path('ninos/', views.ninos, name="categoria-ninos"),
	path('agregar-producto/', views.AgregarProducto.as_view(), name='agregar-producto'),
	path('agregar-producto-success/', views.AgregarProductoSuccess.as_view(), name='agregar-producto-success')
	
	]
