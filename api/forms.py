from django import forms
from .models import (
    Taller, Cliente, Marca, Modelo, TipoVehiculo, Vehiculo, 
    Falla, TipoServicio, Servicio, Mantenimiento, 
    Alerta, HistorialMensaje, RecordatorioMantenimiento, ConfiguracionSistema
)

class BaseBootstrapForm(forms.ModelForm):
    """Clase base para agregar estilos de Bootstrap a los formularios."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

class TallerForm(BaseBootstrapForm):
    class Meta:
        model = Taller
        fields = ['nombre', 'direccion', 'telefono', 'email']

class ClienteForm(BaseBootstrapForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'recibir_alertas']

class MarcaForm(BaseBootstrapForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'descripcion']

class ModeloForm(BaseBootstrapForm):
    class Meta:
        model = Modelo
        fields = ['marca', 'nombre', 'descripcion']

class TipoVehiculoForm(BaseBootstrapForm):
    class Meta:
        model = TipoVehiculo
        fields = ['nombre', 'descripcion']

class VehiculoForm(BaseBootstrapForm):
    class Meta:
        model = Vehiculo
        fields = ['cliente', 'placa', 'marca', 'modelo', 'tipo', 'color', 'año', 'tipo_combustible', 'vin', 'ficha_tecnica', 'revision_tecnica']

class FallaForm(BaseBootstrapForm):
    class Meta:
        model = Falla
        fields = ['vehiculo', 'descripcion', 'estado_falla']

class TipoServicioForm(BaseBootstrapForm):
    class Meta:
        model = TipoServicio
        fields = ['nombre', 'descripcion', 'costo_base']

class ServicioForm(BaseBootstrapForm):
    class Meta:
        model = Servicio
        fields = ['vehiculo', 'tipo_servicio', 'descripcion', 'estado']

class MantenimientoForm(BaseBootstrapForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'tipo_servicio', 'fecha_realizacion', 'fecha_siguiente', 'descripcion', 'realizado_por', 'estado']

class AlertaForm(BaseBootstrapForm):
    class Meta:
        model = Alerta
        fields = ['cliente', 'mensaje', 'tipo_alerta', 'estado']

class HistorialMensajeForm(BaseBootstrapForm):
    class Meta:
        model = HistorialMensaje
        fields = ['cliente', 'mensaje', 'estado_envio']

class RecordatorioMantenimientoForm(BaseBootstrapForm):
    class Meta:
        model = RecordatorioMantenimiento
        fields = ['vehiculo', 'mantenimiento', 'fecha_recordatorio', 'enviado']

class ConfiguracionSistemaForm(BaseBootstrapForm):
    class Meta:
        model = ConfiguracionSistema
        fields = ['taller', 'configuracion_alertas', 'mensaje_ofertas', 'mensaje_mantenimiento', 'intervalo_alertas']
