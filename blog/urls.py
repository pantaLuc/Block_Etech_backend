from django.urls import path
from .views import ArticleAdmin, ArticleWriter, ArtticleViewCreate, CommentAPIView, CommentCreateAPI, ListArticlePublish 
urlpatterns = [
 path('listarticle/',ListArticlePublish.as_view({
     'get':'list_publish_article'
 })),
 path('listArticleCategorie/<int:pk>/',ListArticlePublish.as_view({
     'get':'list_publish_article_category'
 })),
 path('createArticle/' , ArtticleViewCreate.as_view()),
 path('articleWriter/',ArticleWriter.as_view({
     'get':'list_article'
 })),
 path('modifyArticleWriter/<int:pk>/' ,ArticleWriter.as_view({
     'put':'list_article'
     
 })),
  path('deleteArticleWriter/<int:pk>/' ,ArticleWriter.as_view({
     'delete':'delete_article'
 })),
 path('publishArticle/<int:pk>/' ,ArticleAdmin.as_view({
     'put':'publish_article'
 })),
####Comment
 path('createcomment/', CommentCreateAPI.as_view()),
 path('createupdatedelete/<int:pk>',CommentAPIView.as_view())


]