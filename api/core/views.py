from django.shortcuts import render
from .models import Post
from .serializers import *
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
        tag_slug = self.kwargs.get('tag_slug', '').lower()
        # tag = Tag.objects.get(slug=tag_slug)
        # return Post.objects.filter(tags=tag)
        return Post.objects.filter(
            tags__slug=tag_slug
        )


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()


class LastFiveArticlesView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        without_post = self.kwargs.get('post_slug').lower()
        return Post.objects.all().order_by('-pk').exclude(
            slug=without_post
        )[:5]


class FeedBackView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerailizer

    def post(self, request, *args, **kwargs):
        serializer_class = ContactSerailizer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get('name')
            from_email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            send_mail(f'От {name} | {subject}', message, from_email, ['n.b.99322@gmail.com'])
            return Response({"success": "Sent"})
