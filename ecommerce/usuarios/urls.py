from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
	path('login/', views.login_page, name="login"),
	path('logout/', views.logout_page, name="logout"),
	path('register/', views.register, name="register"),
	path('mis-datos/', views.ver_datos, name='ver-datos'),
	path('mis-datos-confirmacion/', views.confirmacion_mis_datos, name='confirmacion-mis-datos')
	]
