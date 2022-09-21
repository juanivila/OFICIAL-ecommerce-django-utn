from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	path('accounts/', include('registration.backends.default.urls')),
	path('admin/', admin.site.urls),
	path('', include('productos.urls')),
	path('usuarios/', include('usuarios.urls')),
  path('__debug__/', include('debug_toolbar.urls')),
	
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

