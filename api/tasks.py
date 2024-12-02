from celery import shared_task
from .models import Mantenimiento
from .utils import send_whatsapp_message

@shared_task
def send_maintenance_reminder():
    # Obtener mantenimientos próximos
    mantenimientos = Mantenimiento.objects.filter(fecha_siguiente__lte='fecha_de_hoy')
    
    for mantenimiento in mantenimientos:
        cliente = mantenimiento.vehiculo.cliente
        message = f"Recordatorio: tu vehículo necesita mantenimiento {mantenimiento.tipo_servicio.nombre}. ¡Agenda tu cita!"
        send_whatsapp_message(cliente.telefono, message)
