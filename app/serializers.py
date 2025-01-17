from rest_framework import serializers
from .models import CustomUser, Profile, Category, Tag, BlogPost, Comment
from django.contrib.auth.models import User

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:   #here meata is necesssary with capitalize
        model = CustomUser    
        fields = "__all__"   #here it inputs all field of models
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        field = '__all__'
class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        view = '__all__'
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
