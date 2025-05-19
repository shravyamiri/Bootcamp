import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def slow_function():
    start = time.time()
    time.sleep(1.5)
    logger.info(f"slow_function took {time.time() - start:.2f}s")

slow_function()
