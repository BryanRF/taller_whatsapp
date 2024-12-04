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
            # Para campos de tipo CheckboxInput, usa 'form-check-input'
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({
                    'class': 'form-check-input',
                })
            else:
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
        widgets = {
            'recibir_alertas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MarcaForm(BaseBootstrapForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class ModeloForm(BaseBootstrapForm):
    class Meta:
        model = Modelo
        fields = ['marca', 'nombre', 'descripcion']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class TipoVehiculoForm(BaseBootstrapForm):
    class Meta:
        model = TipoVehiculo
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class VehiculoForm(BaseBootstrapForm):
    class Meta:
        model = Vehiculo
        fields = [
            'cliente', 'placa', 'marca', 'modelo', 'tipo', 'color', 
            'año', 'tipo_combustible', 'vin', 'ficha_tecnica', 
            'revision_tecnica'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'modelo': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'tipo_combustible': forms.Select(attrs={'class': 'form-select'}),
            'ficha_tecnica': forms.Textarea(attrs={'rows': 3}),
            'revision_tecnica': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class FallaForm(BaseBootstrapForm):
    class Meta:
        model = Falla
        fields = ['vehiculo', 'descripcion', 'estado_falla']
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'estado_falla': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class TipoServicioForm(BaseBootstrapForm):
    class Meta:
        model = TipoServicio
        fields = ['nombre', 'descripcion', 'costo_base']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class ServicioForm(BaseBootstrapForm):
    class Meta:
        model = Servicio
        fields = ['vehiculo', 'tipo_servicio', 'descripcion', 'estado']
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'tipo_servicio': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class MantenimientoForm(BaseBootstrapForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'vehiculo', 'tipo_servicio', 'fecha_realizacion', 
            'fecha_siguiente', 'descripcion', 'realizado_por', 'estado'
        ]
        widgets = {
            'fecha_realizacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_siguiente': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class AlertaForm(BaseBootstrapForm):
    class Meta:
        model = Alerta
        fields = ['cliente', 'mensaje', 'tipo_alerta', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'tipo_alerta': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class HistorialMensajeForm(BaseBootstrapForm):
    class Meta:
        model = HistorialMensaje
        fields = ['cliente', 'mensaje', 'estado_envio']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'estado_envio': forms.Select(attrs={'class': 'form-select'}),
        }

class RecordatorioMantenimientoForm(BaseBootstrapForm):
    class Meta:
        model = RecordatorioMantenimiento
        fields = ['vehiculo', 'mantenimiento', 'fecha_recordatorio', 'enviado']
        widgets = {
            'fecha_recordatorio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'enviado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ConfiguracionSistemaForm(BaseBootstrapForm):
    class Meta:
        model = ConfiguracionSistema
        fields = ['taller', 'configuracion_alertas', 'mensaje_ofertas', 'mensaje_mantenimiento', 'intervalo_alertas']
        widgets = {
            'configuracion_alertas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mensaje_ofertas': forms.Textarea(attrs={'rows': 3}),
            'mensaje_mantenimiento': forms.Textarea(attrs={'rows': 3}),
        }
