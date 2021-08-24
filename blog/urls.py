from django.urls import path
from .views import ArticleAdmin, ArticleWriter, ArtticleViewCreate, CategoryAPIView, CategoryCreateView, CommentAPIView, CommentCreateAPI, ListArticlePublish 
urlpatterns = [
 path('listarticlePublished/',ListArticlePublish.as_view({
     'get':'list_publish_article'
 })),
 path('listArticlePublishedCategorie/<int:pk>/',ListArticlePublish.as_view({
     'get':'list_publish_article_category'
 })),
 path('writerCreateArticle/' , ArtticleViewCreate.as_view()),
 path('articleWriter/',ArticleWriter.as_view({
     'get':'list_article'
 })),
 path('writerModifyArticle/<int:pk>/' ,ArticleWriter.as_view({
     'put':'list_article'
     
 })),
  path('writerDeleteArticle/<int:pk>/' ,ArticleWriter.as_view({
     'delete':'delete_article'
 })),
 path('adminPublishArticle/<int:pk>/' ,ArticleAdmin.as_view({
     'put':'publish_article'
 })),
####Comment
 path('userCreatecomment/', CommentCreateAPI.as_view()),
 path('userCreateUpdateDeleteComment/<int:pk>',CommentAPIView.as_view()),
##### category 
path('adminCreateCategory',CategoryCreateView.as_view()),
path('adminDeleteUptadeRetrieveCategory' ,CategoryAPIView.as_view())


]