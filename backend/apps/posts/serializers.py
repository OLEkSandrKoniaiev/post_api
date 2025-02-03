from rest_framework import serializers

from apps.posts.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = (
            'id',
            'text',
            'user',
        )
        read_only_fields = ('user',)

    def create(self, validated_data: dict):
        validated_data['user'] = self.context['request'].user
        post = PostModel.objects.create(**validated_data)
        return post
