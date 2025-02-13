from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import get_user_model
from django.db.models import F, Q
from django.utils import timezone
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.user.filter import ProfileFilter, UserFilter
from apps.user.models import ProfileModel
from apps.user.permissions import IsSuperUser
from apps.user.serializers import ProfilePhotoSerializer, ProfileSerializer, UserSerializer

UserModel = get_user_model()


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
class UserListCreateView(ListCreateAPIView):
    """
    get:
        Get a list of all users
    post:
        Create a new user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]


class AuthorizedUserListView(ListAPIView):
    """
    get:
        Get a list of authorized users
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        now = timezone.now()
        return UserModel.objects.filter(Q(last_logout__gt=F('last_login')) & Q(last_logout__gt=now))


class UserDestroyView(DestroyAPIView):
    """
    delete:
        Delete a user
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = UserModel.objects.get(id=self.request.user.id)
        return obj


class BlockUserView(GenericAPIView):
    """
    patch:
        Block a user, by making is_active = False
    """

    def get_serializer(self):
        return None

    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):
    """
    patch:
        Unblock a user, by making is_active = True
    """

    def get_serializer(self):
        return None

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    """
    patch:
        Make a user to admin, by making is_staff = True
    """
    permission_classes = [IsSuperUser]

    def get_serializer(self):
        return None

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    """
    patch:
        Make an admin to user, by making is_staff = False
    """
    permission_classes = [IsSuperUser]

    def get_serializer(self):
        return None

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[],
    ),
)
class ProfileListView(ListAPIView):
    """
    get:
        Get a list of all profiles
    """
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    filterset_class = ProfileFilter
    permission_classes = [AllowAny]


class ProfileUpdateView(UpdateAPIView):
    """
    patch:
        Update a profile
    """
    serializer_class = ProfileSerializer
    http_method_names = ['patch']
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = ProfileModel.objects.get(user=self.request.user)
        return obj


class ProfileAddPhotoView(UpdateAPIView):
    """
    put:
        Update a profile photo
    """
    serializer_class = ProfilePhotoSerializer
    http_method_names = ['put']
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = ProfileModel.objects.get(user=self.request.user)
        return obj

    def perform_update(self, serializer):
        profile = self.get_object()
        profile.photo.delete()
        super().perform_update(serializer)
