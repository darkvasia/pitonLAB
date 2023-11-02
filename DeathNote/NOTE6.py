import json
import functools
from datetime import datetime

logs = []

LOG_FILE_PATH = "function_logs.txt"

def write_log_to_file(log):
    """Функція для запису логу у файл."""
    log["time"] = log["time"].strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(json.dumps(log) + "\n")

def logger_with_type(log_type="info"):
    """Декоратор для логування інформації про виклики функцій."""
    def decorator_logger(func):
        @functools.wraps(func)
        def wrapper_logger(*args, **kwargs):
            time = datetime.now()
            result = func(*args, **kwargs)
            log_entry = {
                "time": time,
                "name": func.__name__,
                "args": args,
                "kwargs": kwargs,
                "result": result,
                "log_type": log_type
            }
            logs.append(log_entry)
            write_log_to_file(log_entry) 
            return result
        return wrapper_logger
    return decorator_logger

def get_logs():
    """Генератор для отримання логів."""
    for log in logs:
        yield log

@logger_with_type(log_type="error")
def divide(a, b):
    return a / b

@logger_with_type(log_type="info")
def multiply(a, b):
    return a * b

multiply(3, 4)
divide(4, 2)
multiply(5, 6)

log_gen = get_logs()
print(next(log_gen))
print(next(log_gen))
print(next(log_gen))

