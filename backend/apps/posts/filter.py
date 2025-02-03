from django_filters import rest_framework as filters

from apps.posts.serializers import PostSerializer


class PostFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name='user')

    text_starts_with = filters.CharFilter(field_name='text', lookup_expr='startswith')
    text_ends_with = filters.CharFilter(field_name='text', lookup_expr='endswith')
    text_contains = filters.CharFilter(field_name='text', lookup_expr='icontains')

    order = filters.OrderingFilter(
        fields=PostSerializer.Meta.fields,
    )
