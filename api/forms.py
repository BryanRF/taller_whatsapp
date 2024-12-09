from django import forms
from .models import (
    Taller, Cliente,  Vehiculo,
   Servicio, Mantenimiento
    , HistorialMensaje,  ConfiguracionSistema
)

from django.utils.safestring import mark_safe

class BaseBootstrapForm(forms.ModelForm):
    """Clase base para agregar estilos de Bootstrap y estructura responsiva."""
    def as_div(self):
        """Renderiza cada campo dentro de un div con clases Bootstrap."""
        output = []
        for field_name, field in self.fields.items():
            widget = self[field_name]
            field_classes = 'form-check-input ' if isinstance(field.widget, forms.CheckboxInput) else 'form-control'
            field.widget.attrs.setdefault('class', field_classes)

            # Cambiamos la clase para que los check tengan col-12
            div_class = 'col-12' if isinstance(field.widget, forms.CheckboxInput) else 'col-6'
            
            label = widget.label_tag(attrs={'class': 'form-label'})
            output.append(
                f'<div class="{div_class} mb-3">'
                f'{label}'
                f'{widget}'
                f'</div>'
            )
        return mark_safe(''.join(output))

    def __str__(self):
        return self.as_div()



class ClienteForm(BaseBootstrapForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'recibir_alertas']
        widgets = {
            'recibir_alertas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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



class HistorialMensajeForm(BaseBootstrapForm):
    class Meta:
        model = HistorialMensaje
        fields = ['cliente', 'mensaje', 'estado_envio']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'estado_envio': forms.Select(attrs={'class': 'form-select'}),
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
