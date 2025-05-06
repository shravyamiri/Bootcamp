import logging

# Setup logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define a flag to control debug logging
debug = True

if debug:
    logger.debug("This is a debug message, only shown if debug is True.")
else:
    logger.debug("This message won't be logged because debug is False.")
