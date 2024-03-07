import logging
import platform
from zapish_logger import console_logger


def get_application_logger() -> logging.Logger:
    return console_logger(f'webserver-for-demo-{platform.node()}', log_format='simple')
