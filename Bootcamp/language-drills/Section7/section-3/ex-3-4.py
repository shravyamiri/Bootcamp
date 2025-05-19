import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process():
    logger.debug("Entering process()")
    # Some processing
    logger.debug("Exiting process()")

process()
