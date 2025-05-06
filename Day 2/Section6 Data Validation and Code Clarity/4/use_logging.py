import logging

# Setup the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
