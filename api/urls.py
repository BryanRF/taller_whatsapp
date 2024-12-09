from django.urls import path
from .views import *
from .models import *
from .forms import *
from . import views
from django.contrib.auth.views import LoginView, LogoutView
# Lista de configuraciones para modelos
MODELS_CONFIG = [
    {'model': Cliente, 'form': ClienteForm},
    {'model': Vehiculo, 'form': VehiculoForm},
    {'model': Mantenimiento, 'form': MantenimientoForm},
    {'model': HistorialMensaje, 'form': HistorialMensajeForm},
]

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('', inicio, name='inicio'),  # Página de inicio
    path('enviar-mensajes/', EnviarMensajesAPIView.as_view(), name="enviar-mensajes"),
    
]

# Generación de URLs dinámicas para cada modelo
for config in MODELS_CONFIG:
    model_name = config['model']._meta.model_name
    form_class = config['form']
    urlpatterns += [
        path(f'{model_name}/', GenericListView.as_view(model=config['model']), name=f'{model_name}_list'),
        path(f'{model_name}/crear/', GenericCreateView.as_view(model=config['model'], form_class=form_class), name=f'{model_name}_create'),
        path(f'{model_name}/editar/<int:pk>/', GenericUpdateView.as_view(model=config['model'], form_class=form_class), name=f'{model_name}_edit'),
        path(f'{model_name}/eliminar/<int:pk>/', GenericDeleteView.as_view(model=config['model']), name=f'{model_name}_delete'),
    ]
