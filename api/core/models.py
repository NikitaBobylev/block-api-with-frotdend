from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class PostComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField(max_length=200)
    cteated_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')



