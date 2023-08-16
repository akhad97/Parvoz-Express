from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _




class CustomValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = _('Something went wrong.')

    def __init__(self, msg: str = None, code: int = status_code):

        if msg is None:
            msg = self.default_message

        self.msg = msg
        response = {'success': False, 'code': code, 'message': msg}
        self.detail = response
