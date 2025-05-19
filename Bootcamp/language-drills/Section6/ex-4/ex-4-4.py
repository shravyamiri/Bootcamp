import logging

# Setup the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replacing print with logger
def greet_user(user_name):
    # Instead of print()
    logger.info(f"Hello, {user_name}!")

greet_user("Alice")
