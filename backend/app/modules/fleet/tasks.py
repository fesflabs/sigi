from app.core.celery import celery_app
import time

@celery_app.task(acks_late=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def send_reservation_notification(reservation_id: int, notification_type: str):
    """
    Simula envio de notificação (ex: alerta de 4h ou 2h antes da agenda para o motorista)
    """
    time.sleep(1)
    return f"Notificação do tipo '{notification_type}' enviada para a reserva {reservation_id}."
