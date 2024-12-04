from twilio.rest import Client

# Configuración de Twilio
account_sid = 'tu_account_sid'  # Reemplaza con tu SID de Twilio
auth_token = 'tu_auth_token'    # Reemplaza con tu token de autenticación
whatsapp_from = 'whatsapp:+14155238886'  # El número de WhatsApp proporcionado por Twilio

client = Client(account_sid, auth_token)

def enviar_alerta_whatsapp(cliente_telefono, mensaje):
    """
    Envia un mensaje de alerta al cliente a través de WhatsApp usando Twilio.
    """
    try:
        mensaje = client.messages.create(
            body=mensaje,  # El mensaje que deseas enviar
            from_=whatsapp_from,  # El número de WhatsApp de Twilio
            to=f'whatsapp:{cliente_telefono}'  # El teléfono del cliente con el prefijo "whatsapp:"
        )
        return mensaje.sid  # Devuelve el SID del mensaje para confirmación
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
        return None
