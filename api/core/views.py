from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import pagination, generics
from taggit.models import Tag


# Create your views here.
class ApiPaginator(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    ordering = 'created_at'


class PostViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ApiPaginator


class TagDetailView(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = ApiPaginator
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug'].lower()
        tag = Tag.objects.get(slug=tag_slug)
        return Post.objects.filter(tags=tag)


