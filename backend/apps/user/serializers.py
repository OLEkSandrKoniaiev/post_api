from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.services.email_service import EmailService

from apps.user.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            'id',
            'name',
            'surname',
            'age',
            'created_at',
            'updated_at',
            'user',
            'photo',
        )
        read_only_fields = ('user', 'photo')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'last_logout',
            'created_at',
            'updated_at',
            'profile'
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(user)
        return user


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('photo',)
