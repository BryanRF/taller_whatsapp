from datetime import timedelta, datetime
from twilio.rest import Client
from django.conf import settings
from .models import Mantenimiento, HistorialMensaje


def enviar_mensajes():
    # Configurar el cliente Twilio
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # Buscar mantenimientos con fecha de próxima operación vencida o en el día actual
    hoy = datetime.now()
    mantenimientos = Mantenimiento.objects.filter(
        fecha_siguiente__lte=hoy,
        estado='Pendiente'
    )

    mensajes_enviados_count = 0  # Contador de mensajes exitosos

    for mantenimiento in mantenimientos:
        # Revisar si ya se envió un mensaje en la última semana para este cliente
        ultima_semana = hoy - timedelta(days=7)
        mensajes_enviados = HistorialMensaje.objects.filter(
            cliente=mantenimiento.vehiculo.cliente,
            fecha_envio__gte=ultima_semana
        )

        if mensajes_enviados.exists():
            continue  # Saltar si ya envió un mensaje en la última semana

        # Enviar el mensaje
        try:
            client.messages.create(
                body=f"Estimado cliente, su mantenimiento para el vehículo {mantenimiento.vehiculo.placa} es hoy.",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=mantenimiento.vehiculo.cliente.telefono
            )

            # Guardar en el historial
            HistorialMensaje.objects.create(
                cliente=mantenimiento.vehiculo.cliente,
                mensaje=f"Estimado cliente, su mantenimiento para el vehículo {mantenimiento.vehiculo.placa} es hoy.",
                estado_envio='Exitoso'
            )
            mensajes_enviados_count += 1  # Incrementar contador
        except Exception as e:
            # Si ocurre un error
            HistorialMensaje.objects.create(
                cliente=mantenimiento.vehiculo.cliente,
                mensaje='Error en el envío',
                estado_envio='Fallido'
            )
            print(f"Error al enviar mensaje: {e}")

    return mensajes_enviados_count  # Retornar la cantidad de mensajes exitosos
