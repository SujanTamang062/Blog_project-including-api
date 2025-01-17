from django.db import models
from django.contrib.auth.models import AbstractUser  #here i import abstractuser because there is no more field like is_author so to add like custrom user field i use abstract user

# Create your models here
class CustomUser(AbstractUser):    #here we completely change the user so we changing the user should be keep in settings.pu as well
    is_author = models.BooleanField(default=False)    #this two are created by admin or server and this is also used to give permission to user while selecting
    is_reader = models.BooleanField(default=False)

class Profile(models.Model):   #in this section this is used to modify profile to create porfile
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)   #her models.cascade is write because if there no data exist then it delete whole data of user and it also help to minimize the debug 
    bio = models.TextField(null=True,blank=True)   #here bio is optional you can set null or blank as well
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True)  #optional image profile ppicture ; saved in profile_pics/ folder
    created_at = models.DateTimeField(auto_now_add=True)   #auto_now_add Sets the time only when the object is created.
    update_at = models.DateTimeField(auto_now=True)   #  Sets the time when the object is created and also whenever it's updated
    
class Category(models.Model):   #here category mostly done by admin/server like tech,health etc 
    name = models.CharField(max_length=25)  #here we enter a value like tech,health,etc
    slug = models.SlugField(unique=True,blank=True)    #slug means adding a detail behind the url  https://www.example.org/<<<name>>
    description = models.TextField(blank=True) #here explanation about name like rapid growing tech etc

'''
 differnece between category and tag
 
Category
Name: "Tech"
Slug: "tech"
Description: "Posts about the latest in technology"
Tag:
Name: "Python"
Slug: "python"


Categories are used to broadly organize content, while tags are more specific and allow for filtering or searching by keywords.


Tag model, the tags are typically keywords or words related to the content of the blog
'''


class Tag(models.Model):   #here we use tab because it helps to serch and filters the data by kewords (it also mostly write by admin/server)
    name = models.CharField(max_length=25)   #here name can be set from server/admin or we can set 
    slug = models.SlugField(unique=True)   #here slug is automatically generated from the name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=225)   #here this is write while creating post
    description = models.TextField()   # #here this is write while creating post
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name = 'posts')  #one to many realation 
    created_at = models.DateTimeField(auto_now_add=True)  #created date is not modify it changes only first time therefore we use auto_not_add = True
    updated_at = models.DateField(auto_now=True) #update date is  modify it changes every time therefore we use auto_not = True
    is_published = models.BooleanField(default=False)   
    published_date = models.DateTimeField(null=True,blank=True)
    tags = models.ManyToManyField(Tag)   #here manytomanyfiled is used because a single blog can have multiple like tec+health+enterainment so we used manyto many fiels
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)  #is used here because each blog post belongs to only one category but category can have manye blog post
    
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)  # Links the comment to a user. If the user is deleted, the comment is deleted.
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE, related_name= "comments") # Links the comment to a blog post.
    created_at = models.DateTimeField(auto_now_add=True)   
    content = models.TextField()   #stores the comment
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='Replies')   #allow comment ot have replied(nesed comment), alos null= True and blank = True make it optional , related name = replies accesing replies for comment
    