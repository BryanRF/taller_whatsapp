from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name=f'admin'),  # Ruta para el panel de administración
    path('', include('api.urls')),  # Incluye las rutas del DefaultRouter
]
