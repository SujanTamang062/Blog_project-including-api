from rest_framework import serializers
from .models import  Profile, Category, Tag, BlogPost, Comment
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# class CustomUserSerializers(serializers.ModelSerializer):
#     class Meta:   #here meata is necesssary with capitalize
#         model = User    
#         fields = "__all__"   #here it inputs all field of models
        
        
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
        fields = ['id','name']
        
class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        
        
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']  # Make the 'user' field read-only so that it is still seen in response
        
        
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        
        extra_kwargs = {
            'password':{
                'write_only' : True
            }
        }
        
class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        Fields = ['id','name']
           

        
