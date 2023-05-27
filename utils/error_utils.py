from django.http import JsonResponse

class AppException(Exception):
    def __init__(self, message: str, status: int):
        self.message = message
        self.status = status


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AppException as e:
            return JsonResponse({'message': e.message, 'status': e.status})
        except Exception as e:
            raise e
    return wrapper