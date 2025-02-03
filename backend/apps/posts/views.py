from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.posts.filter import PostFilter
from apps.posts.models import PostModel
from apps.posts.serializers import PostSerializer


class PostListCreateView(ListCreateAPIView):
    """
    get:
        gets a list of all posts
    post:
        create a new post
    """
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    filterset_class = PostFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        get a specific post (accessible to all)
    patch:
        update a specific post (only owner user)
    delete:
        delete a specific post (only owner user)
    """
    serializer_class = PostSerializer
    http_method_names = ['get', 'patch', 'delete']
    queryset = PostModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_object(self):
        obj = super().get_object()

        if self.request.method in ['PATCH', 'DELETE'] and obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")

        return obj
