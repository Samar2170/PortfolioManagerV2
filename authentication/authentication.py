from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth.models import User
import jwt
from rest_framework.authentication import BaseAuthentication

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None
        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        user = User.objects.get(pk=payload['user_id'])
        if not user:
            raise exceptions.AuthenticationFailed('No user matches this token')
        return (user, token)
        