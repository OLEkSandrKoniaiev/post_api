from django.urls import path

from apps.posts.views import PostListCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list_create'),
    path('/<int:pk>', PostRetrieveUpdateDestroyView.as_view(), name='post_retrieve_update_destroy'),
]
