# whatsapp_api.py
import requests
import json

# Configuración de la API de 360Dialog
API_KEY = 'your_360dialog_api_key'  # Aquí va tu API Key de 360Dialog
API_URL = 'https://waba.360dialog.com/v1/messages'  # URL base para la API de 360Dialog

def send_whatsapp_message(to_number, message):
    """
    Función para enviar un mensaje de WhatsApp usando la API de 360Dialog.
    """

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # Estructura del mensaje a enviar
    data = {
        "recipient_type": "individual",  # Enviamos el mensaje a un número individual
        "to": to_number,  # Número de teléfono del destinatario en formato internacional
        "type": "text",  # Tipo de mensaje (en este caso, un mensaje de texto)
        "text": {
            "body": message  # El mensaje a enviar
        }
    }

    # Enviar solicitud POST para enviar el mensaje
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    # Verificar la respuesta
    if response.status_code == 200:
        print("Mensaje enviado exitosamente.")
    else:
        print(f"Error al enviar mensaje: {response.status_code} - {response.text}")

    return response.json()
# En algún lugar en tu aplicación
from whatsapp_api import send_whatsapp_message

# Número de teléfono del destinatario en formato internacional (sin el '+')
to_number = '51912345678'  # Asegúrate de que el número esté en formato internacional sin el '+'
message = '¡Hola! Este es un recordatorio de tu mantenimiento programado para mañana.'

# Enviar el mensaje
send_whatsapp_message(to_number, message)
# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Configuración de Celery para que use Redis como broker
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
# tasks.py
from celery import shared_task
from .whatsapp_api import send_whatsapp_message
from .models import Mantenimiento
from django.utils import timezone

@shared_task
def send_maintenance_reminders():
    """
    Tarea para enviar recordatorios de mantenimiento a los clientes.
    """
    now = timezone.now()
    # Obtener los mantenimientos próximos
    mantenimientos = Mantenimiento.objects.filter(fecha_siguiente__lte=now + timezone.timedelta(days=1))

    for mantenimiento in mantenimientos:
        cliente = mantenimiento.vehiculo.cliente
        message = f"Hola {cliente.nombre}, este es un recordatorio de que su vehículo {mantenimiento.vehiculo.placa} necesita mantenimiento: {mantenimiento.tipo_servicio.nombre}. ¡Agende su cita pronto!"
        send_whatsapp_message(cliente.telefono, message)
