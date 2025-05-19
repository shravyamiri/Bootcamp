import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"timestamp": datetime.now()}
encoded = json.dumps(data, cls=DateTimeEncoder)
print("JSON with datetime:", encoded)
