from django.db import models
from django.utils import timezone

# Create your models here.

class Taller(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20)  # Teléfono único del taller
    email = models.EmailField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)  # Teléfono único del cliente
    recibir_alertas = models.BooleanField(default=True)  # Si el cliente desea recibir alertas
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.marca.nombre} {self.nombre}'
class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    placa = models.CharField(max_length=10, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=30)
    año = models.PositiveIntegerField()
    tipo_combustible = models.CharField(max_length=20, choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel'), ('Electrico', 'Eléctrico')])
    vin = models.CharField(max_length=50, unique=True, blank=True, null=True)
    ficha_tecnica = models.TextField(blank=True, null=True)
    revision_tecnica = models.DateTimeField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.marca.nombre} {self.modelo.nombre} - {self.placa}'
class Falla(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    descripcion = models.TextField()  # Descripción de la falla
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    estado_falla = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('Resuelto', 'Resuelto')], default='Pendiente')

    def __str__(self):
        return f'Falla en {self.vehiculo} - {self.descripcion[:50]}...'
class TipoServicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    costo_base = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Costo base para el servicio

    def __str__(self):
        return self.nombre
class Servicio(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    fecha_servicio = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Costo calculado para el servicio
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado')], default='Pendiente')

    def __str__(self):
        return f'{self.tipo_servicio.nombre} - {self.vehiculo.placa} ({self.fecha_servicio})'
    
class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.SET_NULL, null=True)
    fecha_realizacion = models.DateTimeField()
    fecha_siguiente = models.DateTimeField()  # Fecha del próximo servicio
    descripcion = models.TextField(blank=True, null=True)
    realizado_por = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado')], default='Pendiente')
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Asegúrate de que este campo esté aquí

    def save(self, *args, **kwargs):
        if self.tipo_servicio:
            self.costo = self.tipo_servicio.costo_base
        super(Mantenimiento, self).save(*args, **kwargs)

    def get_costo(self):
        # Retorna el costo con formato decimal (si lo deseas)
        return f"${self.costo:.2f}" if self.costo else "No disponible"
    
    get_costo.short_description = 'Costo'  # Para mostrar un título más amigable en el admin



class Alerta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mensaje = models.TextField()
    tipo_alerta = models.IntegerField(choices=[(1, 'Mantenimiento'), (2, 'Oferta'), (3, 'Recordatorio')])
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Enviado', 'Enviado'), ('Pendiente', 'Pendiente')], default='Pendiente')

    def __str__(self):
        return f'Alerta para {self.cliente} - {self.tipo_alerta} - {self.estado}'
class HistorialMensaje(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado_envio = models.CharField(max_length=20, choices=[('Exitoso', 'Exitoso'), ('Fallido', 'Fallido')])

    def __str__(self):
        return f'Mensaje a {self.cliente} - {self.fecha_envio}'
class RecordatorioMantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    fecha_recordatorio = models.DateTimeField(default=timezone.now)
    enviado = models.BooleanField(default=False)  # Estado del recordatorio

    def __str__(self):
        return f'Recordatorio para {self.vehiculo.placa} - {self.fecha_recordatorio}'
class ConfiguracionSistema(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    configuracion_alertas = models.BooleanField(default=True)
    mensaje_ofertas = models.TextField(blank=True, null=True)
    mensaje_mantenimiento = models.TextField(blank=True, null=True)
    intervalo_alertas = models.IntegerField(default=30)  # Intervalo de días para alertas

    def __str__(self):
        return f'Configuración del Taller {self.taller.nombre}'