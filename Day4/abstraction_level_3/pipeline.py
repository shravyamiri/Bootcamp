# abstraction_level_3/pipeline.py
import yaml
import importlib
from typing import List
from .types import ProcessorFn

def load_pipeline_from_config(config_path: str) -> List[ProcessorFn]:
    """Loads the processing pipeline from a YAML configuration file."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML configuration: {e}")

    pipeline: List[ProcessorFn] = []
    if 'pipeline' in config and isinstance(config['pipeline'], list):
        for step in config['pipeline']:
            if isinstance(step, dict) and 'type' in step:
                import_path = step['type']
                try:
                    module_name, function_name = import_path.rsplit('.', 1)
                    module = importlib.import_module(module_name)
                    processor_func = getattr(module, function_name)
                    if callable(processor_func):
                        # Basic type check (can be improved)
                        if hasattr(processor_func, '__annotations__') and \
                           processor_func.__annotations__.get('line') == str and \
                           processor_func.__annotations__.get('return') == str:
                            pipeline.append(processor_func)
                        else:
                            raise TypeError(f"Processor function '{import_path}' does not match expected signature (str -> str).")
                    else:
                        raise TypeError(f"'{function_name}' in module '{module_name}' is not callable.")
                except ImportError:
                    raise ImportError(f"Could not import module: {module_name} from path: {import_path}")
                except AttributeError:
                    raise AttributeError(f"Function '{function_name}' not found in module '{module_name}'.")
                except TypeError as te:
                    raise te
                except Exception as e:
                    raise Exception(f"An unexpected error occurred while loading '{import_path}': {e}")
            else:
                raise ValueError("Each pipeline step must be a dictionary with a 'type' key.")
    else:
        raise ValueError("The configuration file must contain a 'pipeline' key with a list of processing steps.")

    return pipeline

def apply_pipeline(line: str, pipeline: List[ProcessorFn]) -> str:
    """Applies a list of processor functions to a single line."""
    processed_line = line
    for processor in pipeline:
        processed_line = processor(processed_line)
    return processed_line