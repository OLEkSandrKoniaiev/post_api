from django.urls import path

from apps.auth.views import (
    ActivateUserView,
    ModifiedTokenObtainPairView,
    ModifiedTokenRefreshView,
    RecoveryPasswordView,
    RecoveryRequestView,
    SocketTokenView,
    UserLogoutView
)

urlpatterns = [
    path('', ModifiedTokenObtainPairView.as_view(), name='auth_login'),
    path('/logout', UserLogoutView.as_view(), name='auth_logout'),
    path('/refresh', ModifiedTokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_activate'),
    path('/recovery', RecoveryRequestView.as_view(), name='auth_recovery'),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view(), name='auth_recovery_password'),
    path('/socket', SocketTokenView.as_view(), name='auth_socket'),
]
