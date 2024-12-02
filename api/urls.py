from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TallerViewSet, ClienteViewSet, MarcaViewSet, ModeloViewSet, TipoVehiculoViewSet, 
    VehiculoViewSet, FallaViewSet, TipoServicioViewSet, ServicioViewSet, 
    MantenimientoViewSet, AlertaViewSet, HistorialMensajeViewSet, 
    RecordatorioMantenimientoViewSet, ConfiguracionSistemaViewSet
)

# Crear el enrutador y registrar las vistas
router = DefaultRouter()
router.register(r'talleres', TallerViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'modelos', ModeloViewSet)
router.register(r'tipos-vehiculos', TipoVehiculoViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'fallas', FallaViewSet)
router.register(r'tipos-servicios', TipoServicioViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'mantenimientos', MantenimientoViewSet)
router.register(r'alertas', AlertaViewSet)
router.register(r'historial-mensajes', HistorialMensajeViewSet)
router.register(r'recordatorios-mantenimiento', RecordatorioMantenimientoViewSet)
router.register(r'configuraciones', ConfiguracionSistemaViewSet)

# Incluir las rutas del enrutador en las URL del proyecto
urlpatterns = [
    path('api/', include(router.urls)),
]
