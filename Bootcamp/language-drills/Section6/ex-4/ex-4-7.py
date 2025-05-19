import logging

# Setup logger using __name__ as logger name
logger = logging.getLogger(__name__)

# This is useful to help identify the source of log messages
# when working with larger applications with multiple modules

logger.info("This is a message logged using __name__ as the logger name.")
