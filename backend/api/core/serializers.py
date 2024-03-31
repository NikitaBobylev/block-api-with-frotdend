from dataclasses import field
from rest_framework import serializers, permissions
from rest_framework.response import Response

from .models import Post, PostComment
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User
from taggit.models import Tag
from rest_framework.views import APIView
from django.core.mail import send_mail


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'name',
        lookup_fields = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class ContactSerailizer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})

        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerialiaer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    post = serializers.SlugRelatedField(slug_field='slug', queryset=Post.objects.all())

    class Meta:
        fields = ('post', 'author', 'text')
        model = PostComment
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ("id", "h1", "title", "slug", "description", "content",
                  "image", "created_at", "author", "tags")
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
