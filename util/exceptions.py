from abc import ABCMeta
from rest_framework import status
from rest_framework.exceptions import APIException

class CustomException(APIException):
    status_code = 400
    error_code = 101
    message=None
    success=False

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.message = []
        for arg in args:
            self.message.append(arg)
        if len(self.message)==1:
            self.message = self.message[0]

    def to_dict(self):
        return {
            'success': self.success,
            'error_code': self.error_code,
            'message': self.message
        }

class ValidationException(CustomException):
    status_code = status.HTTP_400_BAD_REQUEST
    error_code = 102
    success=False

class UnauthorizedException(CustomException):
    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = 103
    success=False

class NoContentException(CustomException):
    status_code = status.HTTP_204_NO_CONTENT
    error_code = 104
    success=False