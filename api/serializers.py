from rest_framework import serializers
from .models import (
    Taller, Cliente, Marca, Modelo, TipoVehiculo, Vehiculo, Falla,
    TipoServicio, Servicio, Mantenimiento, Alerta, HistorialMensaje,
    RecordatorioMantenimiento, ConfiguracionSistema
)

# Serializer para el modelo Taller
class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = ('id', 'nombre', 'direccion', 'telefono', 'email', 'fecha_creacion', 'fecha_actualizacion')

# Serializer para el modelo Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'email', 'telefono', 'recibir_alertas', 'fecha_registro', 'fecha_actualizacion')

# Serializer para el modelo Marca
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nombre', 'descripcion')

# Serializer para el modelo Modelo
class ModeloSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()  # Incluir la marca en el serializer

    class Meta:
        model = Modelo
        fields = ('id', 'nombre', 'marca', 'descripcion')

# Serializer para el modelo TipoVehiculo
class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = ('id', 'nombre', 'descripcion')

# Serializer para el modelo Vehiculo
class VehiculoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  # Detalles del cliente asociado
    marca = MarcaSerializer()  # Detalles de la marca
    modelo = ModeloSerializer()  # Detalles del modelo
    tipo = TipoVehiculoSerializer()  # Detalles del tipo de vehículo

    class Meta:
        model = Vehiculo
        fields = (
            'id', 'cliente', 'placa', 'marca', 'modelo', 'tipo', 'color',
            'año', 'tipo_combustible', 'vin', 'ficha_tecnica', 'revision_tecnica',
            'fecha_registro', 'fecha_actualizacion'
        )

# Serializer para el modelo Falla
class FallaSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()  # Detalles del vehículo asociado

    class Meta:
        model = Falla
        fields = ('id', 'vehiculo', 'descripcion', 'fecha_reporte', 'estado_falla')

# Serializer para el modelo TipoServicio
class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = ('id', 'nombre', 'descripcion', 'costo_base')

# Serializer para el modelo Servicio
class ServicioSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()  # Detalles del vehículo asociado
    tipo_servicio = TipoServicioSerializer()  # Detalles del tipo de servicio

    class Meta:
        model = Servicio
        fields = ('id', 'vehiculo', 'tipo_servicio', 'fecha_servicio', 'descripcion', 'costo', 'estado')

# Serializer para el modelo Mantenimiento
class MantenimientoSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()  # Detalles del vehículo
    tipo_servicio = TipoServicioSerializer()  # Detalles del tipo de servicio

    class Meta:
        model = Mantenimiento
        fields = (
            'id', 'vehiculo', 'tipo_servicio', 'fecha_realizacion', 'fecha_siguiente',
            'descripcion', 'realizado_por', 'estado', 'costo'
        )

# Serializer para el modelo Alerta
class AlertaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  # Detalles del cliente

    class Meta:
        model = Alerta
        fields = ('id', 'cliente', 'mensaje', 'tipo_alerta', 'fecha_envio', 'estado')

# Serializer para el modelo HistorialMensaje
class HistorialMensajeSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  # Detalles del cliente

    class Meta:
        model = HistorialMensaje
        fields = ('id', 'cliente', 'mensaje', 'fecha_envio', 'estado_envio')

# Serializer para el modelo RecordatorioMantenimiento
class RecordatorioMantenimientoSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()  # Detalles del vehículo
    mantenimiento = MantenimientoSerializer()  # Detalles del mantenimiento

    class Meta:
        model = RecordatorioMantenimiento
        fields = ('id', 'vehiculo', 'mantenimiento', 'fecha_recordatorio', 'enviado')

# Serializer para el modelo ConfiguracionSistema
class ConfiguracionSistemaSerializer(serializers.ModelSerializer):
    taller = TallerSerializer()  # Detalles del taller

    class Meta:
        model = ConfiguracionSistema
        fields = (
            'id', 'taller', 'configuracion_alertas', 'intervalo_alertas',
            'mensaje_ofertas', 'mensaje_mantenimiento'
        )
