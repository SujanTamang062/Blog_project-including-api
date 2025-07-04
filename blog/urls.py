"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home,RegisterView,LoginView,IndexView,CategoryView,CommentView,ProfileView

urlpatterns = [
    path('home/',home.as_view({'get':'list','post':'create'})),
    path('home/<int:pk>/',home.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
    path('comment/',CommentView.as_view({'get':'list','post':'create'})),
    path('comment/<int:pk>/',CommentView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
    
    path('profile/',ProfileView.as_view({'get':'list','post':'create'})),
    path('profile/<int:pk>/',ProfileView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
    
    path('category/',CategoryView.as_view({'get':'list','post':'create'})),
    path('login/',LoginView.as_view({'post':'create'})),  
    path('register/',RegisterView.as_view({'post':'create'})),  
    path('index/',IndexView.as_view({'get':'list','post':'create'})),  
    path('admin/', admin.site.urls)
]
