import logging

# Setup file logging
logging.basicConfig(
    filename='app.log',  # Log will be written to this file
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Log a message to the file
logger.info("This is a message logged to the file.")
