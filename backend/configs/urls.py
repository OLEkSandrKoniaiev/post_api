from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="PostAPI Doc",
        default_version='v1',
        description="CW",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api/auth', include('apps.auth.urls')),
    path('api/users', include('apps.user.urls')),
    path('api/posts', include('apps.posts.urls')),
    path("api/doc/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
