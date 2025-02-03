from django_filters import rest_framework as filters

from apps.user.serializers import ProfileSerializer, UserSerializer


class UserFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id')

    email_starts_with = filters.CharFilter(field_name='email', lookup_expr='startswith')
    email_ends_with = filters.CharFilter(field_name='email', lookup_expr='endswith')
    email_contains = filters.CharFilter(field_name='email', lookup_expr='icontains')

    order = filters.OrderingFilter(
        fields=UserSerializer.Meta.fields,
    )


class ProfileFilter(filters.FilterSet):
    name_starts_with = filters.CharFilter(field_name='name', lookup_expr='startswith')
    name_ends_with = filters.CharFilter(field_name='name', lookup_expr='endswith')
    name_contains = filters.CharFilter(field_name='name', lookup_expr='icontains')

    surname_starts_with = filters.CharFilter(field_name='name', lookup_expr='startswith')
    surname_ends_with = filters.CharFilter(field_name='name', lookup_expr='endswith')
    surname_contains = filters.CharFilter(field_name='name', lookup_expr='icontains')

    age = filters.NumberFilter(field_name='age')
    age_gt = filters.NumberFilter(field_name='age', lookup_expr='gt')
    age_gte = filters.NumberFilter(field_name='age', lookup_expr='gte')
    age_lt = filters.NumberFilter(field_name='age', lookup_expr='lt')
    age_lte = filters.NumberFilter(field_name='age', lookup_expr='lte')

    order = filters.OrderingFilter(
        fields=ProfileSerializer.Meta.fields,
    )
