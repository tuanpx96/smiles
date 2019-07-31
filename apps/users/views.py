from django.contrib.auth import authenticate

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import TokenSerializer
from apps.users.utils import get_expired_time
from apps.users.models import Token
from apps.users.validator import LoginEmailValidator


class LoginEmailAPI(APIView):

    def post(self, request, format=None):
        validator = LoginEmailValidator(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)

        email = validator.validated_data['email']
        password = validator.validated_data['password']
        user = authenticate(email=email, password=password)

        if not user:
            return Response('Incorrect email or password', status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.create(user=user)
        data = {
            'access_token': token.key,
            'expired_time': get_expired_time(token),
            'user': user
        }

        serializer = TokenSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
