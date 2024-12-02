from rest_framework import viewsets
from .models import (
    Taller, Cliente, Marca, Modelo, TipoVehiculo, Vehiculo, Falla,
    TipoServicio, Servicio, Mantenimiento, Alerta, HistorialMensaje,
    RecordatorioMantenimiento, ConfiguracionSistema
)
from .serializers import (
    TallerSerializer, ClienteSerializer, MarcaSerializer, ModeloSerializer,
    TipoVehiculoSerializer, VehiculoSerializer, FallaSerializer,
    TipoServicioSerializer, ServicioSerializer, MantenimientoSerializer,
    AlertaSerializer, HistorialMensajeSerializer, RecordatorioMantenimientoSerializer,
    ConfiguracionSistemaSerializer
)

# ViewSet para Taller
class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer

# ViewSet para Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# ViewSet para Marca
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

# ViewSet para Modelo
class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

# ViewSet para TipoVehiculo
class TipoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = TipoVehiculo.objects.all()
    serializer_class = TipoVehiculoSerializer

# ViewSet para Vehiculo
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

# ViewSet para Falla
class FallaViewSet(viewsets.ModelViewSet):
    queryset = Falla.objects.all()
    serializer_class = FallaSerializer

# ViewSet para TipoServicio
class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer

# ViewSet para Servicio
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

# ViewSet para Mantenimiento
class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

# ViewSet para Alerta
class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

# ViewSet para HistorialMensaje
class HistorialMensajeViewSet(viewsets.ModelViewSet):
    queryset = HistorialMensaje.objects.all()
    serializer_class = HistorialMensajeSerializer

# ViewSet para RecordatorioMantenimiento
class RecordatorioMantenimientoViewSet(viewsets.ModelViewSet):
    queryset = RecordatorioMantenimiento.objects.all()
    serializer_class = RecordatorioMantenimientoSerializer

# ViewSet para ConfiguracionSistema
class ConfiguracionSistemaViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionSistema.objects.all()
    serializer_class = ConfiguracionSistemaSerializer
