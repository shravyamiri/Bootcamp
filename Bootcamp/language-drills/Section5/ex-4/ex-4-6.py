# WARNING: Do not unpickle data from untrusted sources.
# Pickle can execute arbitrary code and is a security risk.

# Safer alternatives:
# - JSON for basic data (strings, numbers, lists, dicts)
# - `marshal` for internal Python structures (not portable)
# - `dataclasses.asdict()` + json for structured objects

# Use JSON if data is simple and security matters
import json
safe_data = {"a": 1, "b": 2}
json_string = json.dumps(safe_data)
restored = json.loads(json_string)
print("Safe alternative using JSON:", restored)
