from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('login/', views.login, name="login"),
	path('register/', views.register, name="register"),
	path('hombres/', views.categoria_hombres, name="categoria-hombres"),
	
	]
