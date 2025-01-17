from django.contrib import admin
from .models import CustomUser, Profile, Category, Tag, BlogPost, Comment

# Register your models here.
admin.site.register(CustomUser,Profile,Category,Tag,BlogPost,Comment)