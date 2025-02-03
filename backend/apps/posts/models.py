from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

UserModel = get_user_model()


class PostModel(BaseModel):
    class Meta:
        db_table = 'posts'
        ordering = ['-id']

    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
