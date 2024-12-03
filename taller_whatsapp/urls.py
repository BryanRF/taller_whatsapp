from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),  # Incluye las rutas del DefaultRouter
]
