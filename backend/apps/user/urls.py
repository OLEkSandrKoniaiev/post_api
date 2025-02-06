from django.urls import path

from .views import (
    AdminToUserView,
    AuthorizedUserListView,
    BlockUserView,
    ProfileAddPhotoView,
    ProfileListView,
    ProfileUpdateView,
    UnBlockUserView,
    UserDestroyView,
    UserListCreateView,
    UserToAdminView
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/delete', UserDestroyView.as_view(), name='user_destroy'),
    path('/online', AuthorizedUserListView.as_view(), name='user_online'),
    path('/<int:pk>/block', BlockUserView.as_view(), name='user_block'),
    path('/<int:pk>/unblock', UnBlockUserView.as_view(), name='user_unblock'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/profiles', ProfileListView.as_view(), name='profile_list'),
    path('/profiles/patch', ProfileUpdateView.as_view(), name='profile_update'),
    path('/profiles/add_photo', ProfileAddPhotoView.as_view(), name='profile_photos'),
]
