from functools import wraps
from datetime import datetime

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().isoformat()}] Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper