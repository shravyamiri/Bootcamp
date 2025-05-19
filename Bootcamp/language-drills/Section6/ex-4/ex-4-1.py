import logging

# Setup the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log an informational message
logger.info("This is an informational message.")

# Example of logging variables
user_name = "Alice"
logger.info(f"User {user_name} has logged in.")
