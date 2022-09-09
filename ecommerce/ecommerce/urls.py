from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('accounts/', include('registration.backends.default.urls')),
	path('admin/', admin.site.urls),
	path('', include('productos.urls')),
	path('usuarios/', include('usuarios.urls')),
	
	]
