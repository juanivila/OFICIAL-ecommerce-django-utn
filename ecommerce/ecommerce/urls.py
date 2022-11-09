from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	
	# My Apps
	path('', include('productos.urls')),
	path('usuarios/', include('usuarios.urls')),
	path('contacto/', include('contacto.urls')),
	
	# Other apps
	path('accounts/', include('registration.backends.default.urls')),
	path('__debug__/', include('debug_toolbar.urls')),
	path('captcha/', include('captcha.urls')),
	
	]

if settings.DEBUG:
	from django.conf.urls.static import static
	
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
