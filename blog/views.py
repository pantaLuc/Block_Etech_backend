from collections import UserList
from django.db.models import query
from django.http import response
from blog.models import Article, Article_tag, Category, Comment, Like, Tag
from django.shortcuts import render
from users.models import User
from .serializers import ArticleSerializer, Article_tagSerializer, CategorySerializer, CommentSerializer, LikeSerializer, TagSerializer
from users.serializers import UserDetailsSerializer
from rest_framework.response import Response
from rest_framework import generics,permissions, serializers ,viewsets,status
from rolepermissions.mixins import HasRoleMixin
from rolepermissions.mixins import HasPermissionsMixin
from rest_framework.permissions import IsAuthenticated
from rolepermissions.decorators import has_role_decorator
from rolepermissions.roles import assign_role
# Create your views here.

class ArtticleViewCreate(HasRoleMixin,generics.CreateAPIView):
   allowed_roles = 'writer'
   queryset=Article.objects.all()
   serializer_class=ArticleSerializer

class ArticleViewRetrieve(HasRoleMixin ,generics.RetrieveAPIView):
    allowed_roles =['user'] 
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArticleWriter( HasRoleMixin,viewsets.ViewSet):
   permission_classes = [IsAuthenticated]
   allowed_roles = 'writer'

   def updateArticle(self ,request ,pk=None):
      article=Article.objects.get(user=pk)
      serializer=UserDetailsSerializer(instance=article ,data=request.data ,partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
   def list_article(self ,request , pk):
      queryset=Article.objects.filter(user=pk).all
      serializer=ArticleSerializer(queryset,many=True)
      return Response(serializer.data)
   def delete_article(self ,request ,pk):
      article=Article.objects.get(user=pk)
      article.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
   
class ArticleAdmin(HasRoleMixin, viewsets.ViewSet):
   allowed_roles = 'admin'
   def publish_article(self ,request,pk):
      article=Article.objects.get(pk)
      if article.status !='published':
         article.status='published'
         article.save()
      else:
         return Response({
            'message':'article est deja publie'
         })
      return Response(status=status.HTTP_202_ACCEPTED)
   
     
class ListArticlePublish(viewsets.ViewSet):
   def list_publish_article(self ,request):
      queryset=Article.objects.filter(status='published').all()
      serializers=ArticleSerializer(queryset,many=True)
      return Response(serializers.data)
   def list_publish_article_category(self ,request ,pk):
      queryset=Article.objects.filter(category=pk).all()
      serializers=ArticleSerializer(queryset ,many=True)
      return Response(serializers.data)


### Category 
class CategoryCreateView(HasRoleMixin,generics.CreateAPIView):
      allowed_roles='admin'
      queryset=Category.objects.all()
      serializer_class=CategorySerializer
class CategoryAPIView(HasRoleMixin ,generics.RetrieveUpdateDestroyAPIView):
   allowed_roles='admin'
   queryset=Category.objects.all()
   serializer_class=CategorySerializer


###class Comment 
class TagCreateView(HasRoleMixin ,generics.CreateAPIView):
   allowed_roles='admin'
   queryset=Tag.objects.all()
   serializer_class=TagSerializer
class TagAPIView(HasRoleMixin ,generics.RetrieveUpdateDestroyAPIView):
   allowed_roles='admin'
   queryset=Tag.objects.all()
   serializer_class=TagSerializer
class Article_Tage(HasRoleMixin,generics.RetrieveAPIView):
   allowed_roles='user'
   queryset=Article_tag.objects.all()
   serializer_class=Article_tagSerializer

#### Comment 
class CommentAPIView(HasRoleMixin ,generics.RetrieveUpdateDestroyAPIView):
      allowed_roles = 'user'
      queryset=Comment.objects.all()
      serializer_class=CommentSerializer
class CommentCreateAPI(HasRoleMixin ,generics.CreateAPIView):
   allowed_roles = 'user'
   queryset=Comment.objects.all()
   serializer_class=CommentSerializer
#####Like 
class LikeCreate(HasRoleMixin ,generics.CreateAPIView):
   allowed_roles='user'
   queryset=Like.objects.all()
   serializer_class=LikeSerializer
class DisLIke(generics.DestroyAPIView):
   allowed_role='user'
   queryset=Like.objects.all()
   serializer_class=LikeSerializer

class ChangeUserRole(viewsets.ViewSet):
   pass