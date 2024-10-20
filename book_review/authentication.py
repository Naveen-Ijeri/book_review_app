from rest_framework import authentication
from rest_framework import exceptions
from utils import ErrorResponse
from constant import ErrorMessage


class AuthenticateUser(authentication.BaseAuthentication):

    def authenticate(self, request):
        if not request.is_token_valid:
            raise exceptions.AuthenticationFailed(ErrorResponse.get_response_obj(
                ErrorResponse.AUTHENTICATION_ERROR,
                ErrorMessage.INVALID_TOKEN
            )
            )