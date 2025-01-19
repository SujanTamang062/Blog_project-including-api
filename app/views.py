from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import CustomUser, Profile, Category, Tag, BlogPost, Comment
from rest_framework import viewsets, status
from app.serializers import CategorySerializers, ProfileSerializers, BlogPostSerializers, CommentSerializers, CustomUserSerializers, TagSerializers, UserSerializers
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.contrib.auth import logout
from django.contrib.redirects.models import Redirect
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response



class home(ModelViewSet):   #here pagination/filtering/CRUD will work
    queryset = BlogPost.objects.all()
    serializer_class = CategorySerializers      #here i should add pagination,searching,filtering,permission
    
class RegisterView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def create(request,self):
        password = request.data.get("password")
        hash_password = make_password(password)
        data = data.copy()
        data[password]=hash_password
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
class LoginView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def create(request,self):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username = username,password=password)
        if user!=None:
            login(request,user)
            return Redirect(home)
        user_form_obj = UserSerializers()
        data = {'form':user_form_obj}    
        return render(request,'login.html',context=data)  
    
class IndexView(ModelViewSet):  #here permission,login,register will work
    queryset = BlogPostSerializers
    serializer_class = BlogPostSerializers   
    
def LogoutView(request):
    logout(request)
    Redirect("index.html")
    
    