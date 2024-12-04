from django import template

register = template.Library()

@register.filter
def get_field_value(obj, field_name):
    """
    Accede a un campo dinámicamente en el objeto.
    """
    try:
        return getattr(obj, field_name, 'No disponible')  # Devuelve 'No disponible' si el campo no existe
    except AttributeError:
        return 'No disponible'
