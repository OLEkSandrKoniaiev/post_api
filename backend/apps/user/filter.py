from django_filters import rest_framework as filters

from django.contrib.auth import get_user_model

from apps.user.serializers import ProfileSerializer, UserSerializer

UserModel = get_user_model()


class UserFilter(filters.FilterSet):
    id = filters.NumberFilter()

    email_starts_with = filters.CharFilter(field_name='email', lookup_expr='startswith')
    email_ends_with = filters.CharFilter(field_name='email', lookup_expr='endswith')
    email_contains = filters.CharFilter(field_name='email', lookup_expr='contains')

    order = filters.OrderingFilter(
        fields=UserSerializer.Meta.fields,
    )


class ProfileFilter(filters.FilterSet):
    name_starts_with = filters.CharFilter(field_name='name', lookup_expr='startswith')
    name_ends_with = filters.CharFilter(field_name='name', lookup_expr='endswith')
    name_contains = filters.CharFilter(field_name='name', lookup_expr='contains')

    surname_starts_with = filters.CharFilter(field_name='name', lookup_expr='startswith')
    surname_ends_with = filters.CharFilter(field_name='name', lookup_expr='endswith')
    surname_contains = filters.CharFilter(field_name='name', lookup_expr='contains')

    age = filters.NumberFilter()
    age_gt = filters.NumberFilter(field_name='age', lookup_expr='gt')
    age_gte = filters.NumberFilter(field_name='age', lookup_expr='gte')
    age_lt = filters.NumberFilter(field_name='age', lookup_expr='lt')
    age_lte = filters.NumberFilter(field_name='age', lookup_expr='lte')

    order = filters.OrderingFilter(
        fields=ProfileSerializer.Meta.fields,
    )
