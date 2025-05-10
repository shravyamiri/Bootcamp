import yaml
import importlib
from typing import List
from types import ModuleType, FunctionType
from .types import ProcessorFn
  # Correct import for ProcessorFn from your own types.py


def load_pipeline(config_path: str) -> List[ProcessorFn]:
    """Load and return the pipeline steps dynamically from the config"""
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Config file '{config_path}' not found.")
        raise
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        raise

    pipeline = []
    for step in config['pipeline']:
        path = step['type']
        module_path, func_name = path.rsplit('.', 1)

        try:
            # Dynamically import the module and get the function
            module: ModuleType = importlib.import_module(module_path)
            func: FunctionType = getattr(module, func_name)

            # Check if the function is callable
            if not callable(func):
                raise TypeError(f"{func_name} is not callable")

            # Add function to the pipeline
            pipeline.append(func)
        except (ImportError, AttributeError, TypeError) as e:
            # Catch all errors related to import and function retrieval
            print(f"Error loading '{path}': {e}")
            raise  # Reraise to terminate the program

    return pipeline
