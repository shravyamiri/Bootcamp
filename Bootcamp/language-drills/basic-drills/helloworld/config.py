import os
import yaml
import logging

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "num_times": 1
}

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "_default_config.yaml")

def load_config():
    paths = [os.getcwd()]
    config_env = os.getenv("CONFIG_PATH")
    if config_env:
        paths.extend(config_env.split(":"))
    paths.append(DEFAULT_PATH)

    for path in paths:
        try:
            file_path = os.path.join(path, "_config.yaml") if not path.endswith(".yaml") else path
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    config = yaml.safe_load(f)
                    logger.debug(f"Loaded config from {file_path}: {config}")
                    return config
        except Exception as e:
            logger.error(f"Error loading config from {path}: {e}")

    logger.warning("No config found. Using default.")
    return DEFAULT_CONFIG
