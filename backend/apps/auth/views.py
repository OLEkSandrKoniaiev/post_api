from configs.extra_conf import SIMPLE_JWT
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken, SocketToken

from apps.auth.serializers import EmailSerializer, LogoutSerializer, PasswordSerializer
from apps.user.serializers import UserSerializer

UserModel = get_user_model()


@method_decorator(
    name='patch',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
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


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
class RecoveryRequestView(GenericAPIView):
    """
    post:
        Sending a request to get the token
    """
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def get_serializer(self):
        return None

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=serializer.data['email'])
        EmailService.recovery(user)
        return Response({'details': 'link send to email'}, status.HTTP_200_OK)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
class RecoveryPasswordView(GenericAPIView):
    """
    post:
        Sending a token to change the password
    """
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def get_serializer(self):
        return None

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
    """
    get:
        Get token for socket connection
    """
    permission_classes = [IsAuthenticated]

    def get_serializer(self):
        return None

    def get(self, *args, **kwargs):
        token = JWTService.create_token(user=self.request.user, token_class=SocketToken)
        return Response({'token': str(token)}, status.HTTP_200_OK)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
class ModifiedTokenObtainPairView(TokenObtainPairView):
    """
    post:
        Sending credentials for login
    """

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        email = request.data['email']

        if email:
            try:
                user = UserModel.objects.get(email=email)
                user.last_logout = timezone.now() + SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
                user.save()
            except UserModel.DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return response


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
class ModifiedTokenRefreshView(TokenRefreshView):
    """
    post:
        Sending refresh token to get new token pair
    """

    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.data['refresh']

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                user = UserModel.objects.get(id=token['user_id'])
                user.last_login = timezone.now()
                user.last_logout = timezone.now() + SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
                user.save()
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        response = super().post(request, *args, **kwargs)
        return response


class UserLogoutView(UpdateAPIView):
    """
    patch:
        Logout the user
    """
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh"]
        token = RefreshToken(refresh_token)

        user = get_object_or_404(UserModel, id=token['user_id'])
        user.last_logout = timezone.now()
        user.save()

        token.blacklist()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
