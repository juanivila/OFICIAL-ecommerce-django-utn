from django.urls import path
from productos import views

urlpatterns = [
	path('', views.home),
	]
