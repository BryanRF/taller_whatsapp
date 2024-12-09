import logging
from django_cron import CronJobBase, Schedule
from api.services import enviar_mensajes

logger = logging.getLogger('django')
        
class EnviarMensajesJob(CronJobBase):
    def __init__(self):
        self.SCHEDULE = Schedule(run_every=3600)  # ejecuta cada hora
        code = 'enviar_mensajes_cron'
    def do(self):
        logger.info('Se ejecutó el cron de enviar mensajes')
        enviar_mensajes()