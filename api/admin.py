from django.contrib import admin
from .models import (
    Taller, Cliente, Marca, Modelo, TipoVehiculo, Vehiculo, Falla,
    TipoServicio, Servicio, Mantenimiento, Alerta, HistorialMensaje, 
    RecordatorioMantenimiento, ConfiguracionSistema
)

# Registrar el modelo Taller
@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre', 'telefono', 'email')
    list_filter = ('fecha_creacion',)

# Registrar el modelo Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'recibir_alertas', 'fecha_registro')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('recibir_alertas', 'fecha_registro')

# Registrar el modelo Marca
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Registrar el modelo Modelo
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'descripcion')
    search_fields = ('nombre', 'marca__nombre')
    list_filter = ('marca',)

# Registrar el modelo TipoVehiculo
@admin.register(TipoVehiculo)
class TipoVehiculoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Registrar el modelo Vehiculo
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'cliente', 'marca', 'modelo', 'tipo', 'color', 'año', 'tipo_combustible', 'vin', 'fecha_registro')
    search_fields = ('placa', 'vin', 'cliente__nombre', 'marca__nombre', 'modelo__nombre')
    list_filter = ('marca', 'modelo', 'tipo', 'tipo_combustible', 'fecha_registro')

# Registrar el modelo Falla
@admin.register(Falla)
class FallaAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'descripcion', 'fecha_reporte', 'estado_falla')
    search_fields = ('vehiculo__placa', 'descripcion', 'estado_falla')
    list_filter = ('estado_falla', 'fecha_reporte')

# Registrar el modelo TipoServicio
@admin.register(TipoServicio)
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'costo_base')
    search_fields = ('nombre',)
    list_filter = ('nombre',)

# Registrar el modelo Servicio
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'tipo_servicio', 'fecha_servicio', 'costo', 'estado')
    search_fields = ('vehiculo__placa', 'tipo_servicio__nombre')
    list_filter = ('estado', 'fecha_servicio', 'tipo_servicio')

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'tipo_servicio', 'fecha_realizacion', 'fecha_siguiente', 'estado', 'get_costo')
    search_fields = ('vehiculo__placa', 'tipo_servicio__nombre')
    list_filter = ('estado', 'fecha_realizacion')


 # Para que tenga un título adecuado en la interfaz

# Registrar el modelo Alerta
@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'mensaje', 'tipo_alerta', 'fecha_envio', 'estado')
    search_fields = ('cliente__nombre', 'mensaje')
    list_filter = ('tipo_alerta', 'estado', 'fecha_envio')

# Registrar el modelo HistorialMensaje
@admin.register(HistorialMensaje)
class HistorialMensajeAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'mensaje', 'fecha_envio', 'estado_envio')
    search_fields = ('cliente__nombre', 'mensaje')
    list_filter = ('estado_envio', 'fecha_envio')

# Registrar el modelo RecordatorioMantenimiento
@admin.register(RecordatorioMantenimiento)
class RecordatorioMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'mantenimiento', 'fecha_recordatorio', 'enviado')
    search_fields = ('vehiculo__placa',)
    list_filter = ('enviado', 'fecha_recordatorio')

# Registrar el modelo ConfiguracionSistema
@admin.register(ConfiguracionSistema)
class ConfiguracionSistemaAdmin(admin.ModelAdmin):
    list_display = ('taller', 'configuracion_alertas', 'intervalo_alertas', 'mensaje_ofertas', 'mensaje_mantenimiento')
    search_fields = ('taller__nombre',)
    list_filter = ('configuracion_alertas',)

