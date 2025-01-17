from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CustomUser, Profile, Category, Tag, BlogPost, Comment
from rest_framework import viewsets, status
from serializers import CategorySerializers, ProfileSerializers, BlogPostSerializers, CommentSerializers, CustomUserSerializers, TagSerializers, UserSerializers



class home(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = CategorySerializers
class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
class LoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
class IndexView(viewsets.ModelViewSet):
    queryset = BlogPostSerializers
    serializer_class = BlogPostSerializers