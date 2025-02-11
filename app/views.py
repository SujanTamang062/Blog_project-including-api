from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile, Category, BlogPost, Comment
from rest_framework import status
from app.serializers import CategorySerializers, ProfileSerializers, BlogPostSerializers, CommentSerializers, UserSerializers
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from .permissions import OwnershipCheck

# from rest_framework.pagination import PageNumberPagination
# class CustomPagination(PageNumberPagination):
#     page_size = 2

class home(ModelViewSet):   #here pagination/filtering/CRUD will work
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers      #here i should add pagination,searching,filtering,permission
    #Redirect 'home'
    permission_classes = [DjangoModelPermissions,IsAuthenticated,OwnershipCheck]
    # pagination_class = CustomPagination
    
    def perform_create(self,serailizer):
        serailizer.save(author = self.request.user)  #automatically assign the logged in user as the owner of the post
        
    filterset_fields = ['created_at','category','author','id']
    search_fields = ['title','category__name','author__username','id']
    ordering = ['-created_at']
 
    
class RegisterView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []
        
    def create(self,request):
        password = request.data.get("password")
        hash_password = make_password(password)
        data = request.data.copy()
        data['password']=hash_password
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
class LoginView(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []
    def create(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username = username,password=password)
        
        if user == None:
            return Response({'detail':"invallid Creditinails"},status=status.HTTP_401_UNAUTHORIZED) 

        else:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=status.HTTP_200_OK)
        
        
class IndexView(ModelViewSet):  #here permission,login,register will work
    queryset = BlogPostSerializers
    serializer_class = BlogPostSerializers   
    


class CategoryView(ModelViewSet):   #here pagination/filtering/CRUD will work
    queryset = Category.objects.all()
    serializer_class = CategorySerializers      #here i should add pagination,searching,filtering,permission
    
class CommentView(ModelViewSet):   #here pagination/filtering/CRUD will work
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers      #here i should add pagination,searching,filtering,permission
    #Redirect 'home'
    permission_classes = [DjangoModelPermissions,IsAuthenticated,OwnershipCheck]
    # pagination_class = CustomPagination
    
    def perform_create(self,serailizer):
        serailizer.save(user = self.request.user)  #automatically assign the logged in user as the owner of the post
        
    

    ordering = ['-created_at']
   
   
class ProfileView(ModelViewSet):   #here pagination/filtering/CRUD will work
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers      #here i should add pagination,searching,filtering,permission
    #Redirect 'home'
    permission_classes = [DjangoModelPermissions,IsAuthenticated,OwnershipCheck]
    # pagination_class = CustomPagination
    
    def perform_create(self,serailizer):
        serailizer.save(user = self.request.user)  #automatically assign the logged in user as the owner of the post
        
    

    ordering = ['-created_at']

