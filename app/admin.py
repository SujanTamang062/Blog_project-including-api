from django.contrib import admin
from .models import CustomUser, Profile, Category, Tag, BlogPost, Comment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(Comment)