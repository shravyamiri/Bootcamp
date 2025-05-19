import logging
import os

DEBUG = os.getenv("DEBUG", "False") == "True"

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)
logger = logging.getLogger(__name__)

logger.debug("Debug mode is enabled")
logger.info("This always logs")
