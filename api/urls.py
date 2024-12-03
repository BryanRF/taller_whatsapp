from django.urls import path
from .views import inicio, GenericListView, GenericCreateView
from .models import Cliente, Vehiculo, Mantenimiento, Alerta, HistorialMensaje
from .forms import ClienteForm, VehiculoForm, MantenimientoForm, AlertaForm, HistorialMensajeForm

# Lista de configuraciones para modelos
MODELS_CONFIG = [
    {'model': Cliente, 'form': ClienteForm},
    {'model': Vehiculo, 'form': VehiculoForm},
    {'model': Mantenimiento, 'form': MantenimientoForm},
    {'model': Alerta, 'form': AlertaForm},
    {'model': HistorialMensaje, 'form': HistorialMensajeForm},
]

urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio
]


for config in MODELS_CONFIG:
    model_name = config['model']._meta.model_name
    urlpatterns += [
        path(f'{model_name}/', GenericListView.as_view(model=config['model']), name=f'{model_name}_list'),
        path(f'{model_name}/crear/', GenericCreateView.as_view(model=config['model'], form_class=config['form']), name=f'{model_name}_create'),
    ]
    print (model_name)
