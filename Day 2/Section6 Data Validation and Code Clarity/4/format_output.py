import logging

# Setup logger with specific format including timestamp and severity level
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Log a message
logger.info("This is an info message with a timestamp and severity level.")
