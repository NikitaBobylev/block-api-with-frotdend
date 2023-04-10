from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash='optional')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('tags/<slug:tag_slug>/', TagDetailView.as_view(), name='tag'),
]

urlpatterns += router.urls
