from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CustomUser, Profile, Category, Tag, BlogPost, Comment
from rest_framework import viewsets, status
from serializers import CategorySerializers, ProfileSerializers, BlogPostSerializers, CommentSerializers, CustomUserSerializers, TagSerializers, UserSerializers
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class home(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = CategorySerializers
class RegisterView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
class LoginView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
class IndexView(ModelViewSet):
    queryset = BlogPostSerializers
    serializer_class = BlogPostSerializers