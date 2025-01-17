from django.db import models
from django.contrib.auth.models import AbstractUser  #here i import abstractuser because there is no more field like is_author so to add like custrom user field i use abstract user

# Create your models here
class CustomUser(AbstractUser):    #here we completely change the user so we changing the user should be keep in settings.pu as well
    is_author = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True)   #here bio is optional you can set null or blank as well
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True)  #optional image profile ppicture ; saved in profile_pics/ folder
    created_at = models.DateTimeField(auto_now_add=True)   #auto_now_add Sets the time only when the object is created.
    update_at = models.DateTimeField(auto_now=True)   #  Sets the time when the object is created and also whenever it's updated
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name = 'posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE, related_name= "comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='Replies')
    