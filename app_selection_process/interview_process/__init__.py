from .views import interviews, selection_process
from .views_tecnical import tecnical
import logging
from .utils_gcp.gcp_pub_sub import GCP

__all__ = ['interviews', 'tecnical', 'selection_process']


def subscriber_message(app):
    logging.warning(f'Watch! GCP')
    leer = GCP()
    leer.subscriber_message(app)
