from django.contrib.auth.models import User
from jwt import ExpiredSignatureError, DecodeError
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
import jwt
from rest_framework.authentication import SessionAuthentication
from course_world.settings import SECRET_KEY


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != 'jwt' or len(auth) == 1 or len(auth) > 2:
            raise AuthenticationFailed("JWT Invalid Header")
        token = auth[1]
        if token == "null":
            raise AuthenticationFailed('Null token not allowed')
        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY)
        except (ExpiredSignatureError, DecodeError) as err:
            raise AuthenticationFailed(err)
        user_id = payload.get("user_id")
        user = User.objects.get(
            id=user_id,
            is_active=True
        )

        if not user:
            raise AuthenticationFailed("Expired JWT token")
        return user, None


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening