import logging

__version__ = '1.0'

log = logging.getLogger(__name__)

API = "https://api.telegram.org/bot{token}/{method}"
FILE = "https://api.telegram.org/file/bot{token}/{method}"