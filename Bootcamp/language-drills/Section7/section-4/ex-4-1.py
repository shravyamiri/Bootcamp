import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def login(user_id):
    logger.info(f"[user_id={user_id}] Function: login - User logged in")

login("U123")
