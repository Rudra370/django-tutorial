from typing import Type

from rest_framework_dataclasses.serializers import DataclassSerializer
from utils.error_utils import AppException

def validator(dataclass: Type[any] = None):
    '''Decorator to validate request body'''

    def get_first_error(serializer_errors, fields=[]):
        '''
            # Example serializer_errors
            {
                'industry': {
                    0: {
                        'value': [ErrorDetail(string = 'This field is required.', code = 'required')]
                    }
                },
                'location': {
                    0: {
                        'value': {
                            'state': [ErrorDetail(
                                string = 'This field may not be null.', code = 'null')],
                            'city': [ErrorDetail(string = 'This field may not be null.', code = 'null')]
                        }
                    }
                }
            }
        '''
        field = list(serializer_errors.keys())[0]
        if not isinstance(field, int):
            fields.append(field)
        errors = serializer_errors[field]

        if isinstance(errors, dict):
            return get_first_error(errors, fields)
        else:
            return fields, str(errors[0])

    def decorator(func):
        def wrapper(*args, **kwargs):
            request = args[1]
            serializer = DataclassSerializer(
                data=request.data, dataclass=dataclass)
            if not serializer.is_valid():
                # error_fields = get_fields_from_error(serializer.errors, [])

                # error_message = ".".join(
                #     error_fields) + ": " + get_first_error_message(serializer.errors)
                error_fields, error_message = get_first_error(
                    serializer.errors, [])
                error_message = ".".join(
                    error_fields) + ": " + error_message
                raise AppException(message=error_message,
                                   status=400)
            obj = dataclass.from_dict(request.data)
            kwargs['body'] = obj
            return func(*args, **kwargs)
        return wrapper
    return decorator
