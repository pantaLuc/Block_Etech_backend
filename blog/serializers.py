from rest_framework import serializers 
from .models import Article, Article_category, Comment, Category, Like, Tag, Article_category, Article_tag
from users.models import User
from rest_framework import serializers
from users.serializers import UserDetailsSerializer
from rest_framework.serializers import SerializerMethodField


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','user' ,'title' ,'slug' ,'description' ,'body' ,'category' ,'publish_at','created_at','updated_at','status')
        model=Article



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'contain', 'article', 'user', 'created_at')



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('tilte', 'description' ,'slug' ,'description' ,'created_at')



class LikeSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        model = Like
        fields = ('id', 'user', 'article')



class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id', 'title' ,'slug' ,'created_at' )



class Article_tagSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    tag = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        model = Article_tag
        fields = ['article', 'tag']