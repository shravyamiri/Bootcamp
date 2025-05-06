import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def process_data():
    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("ERR1001: Division by zero error")

process_data()
