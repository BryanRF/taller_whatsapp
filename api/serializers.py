from rest_framework import serializers
from .models import Cliente, Vehiculo, Mantenimiento, Alerta, HistorialMensaje

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'recibir_alertas', 'fecha_registro']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'cliente', 'placa', 'marca', 'modelo', 'tipo', 'color', 'año', 'tipo_combustible', 'vin', 'revision_tecnica']

class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = ['id', 'vehiculo', 'tipo_servicio', 'fecha_realizacion', 'fecha_siguiente', 'descripcion', 'realizado_por', 'estado']

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = ['id', 'cliente', 'mensaje', 'tipo_alerta', 'fecha_envio', 'estado']

class HistorialMensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialMensaje
        fields = ['id', 'cliente', 'mensaje', 'fecha_envio', 'estado_envio']
