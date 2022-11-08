from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
	path('hombres/', views.hombres, name="categoria-hombres"),
	path('mujeres/', views.mujeres, name="categoria-mujeres"),
	path('ninos/', views.ninos, name="categoria-ninos"),
	
	]
