import logging

# Setup the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Example with contextual message
user = {"name": "Alice", "age": 30}
logger.debug(f"User: {user['name']}, Age: {user['age']}")
