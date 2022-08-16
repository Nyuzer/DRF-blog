from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ('id', 'title', 'body', 'author', 'created_at',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
