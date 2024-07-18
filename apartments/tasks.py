from celery import shared_task
import time
from users.models import User
from users.serializers import UserSerializer
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def calculate_monthly_rent(apartment, month):
    pass

