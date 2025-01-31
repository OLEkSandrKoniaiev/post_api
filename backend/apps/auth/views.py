from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken, SocketToken

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.user.serializers import UserSerializer

UserModel = get_user_model()


# TODO: реалізувати адекватну активацію для користувача
class ActivateUserView(GenericAPIView):
    """
    patch:
        Send activate token to user.
    """
    queryset = UserModel.objects.none()
    permission_classes = [AllowAny]
    http_method_names = ['patch']

    def get_serializer(self, *args, **kwargs):
        return None

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


# TODO: так само реалізувати адекватно відновлення паролю, доробити представленя
class RecoveryRequestView(GenericAPIView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=serializer.data['email'])
        EmailService.recovery(user)
        return Response({'details': 'link send to email'}, status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.verify_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class SocketTokenView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        token = JWTService.create_token(user=self.request.user, token_class=SocketToken)
        return Response({'token': str(token)}, status.HTTP_200_OK)
