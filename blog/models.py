from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User ,related_name="categories", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200)
    description = models.TextField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_at']



class Tag(models.Model): 
    author  = models.ForeignKey(User ,related_name="user_tags", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_at']

class Article(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

    user = models.ForeignKey(User ,related_name="posts_user", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200)
    description = models.TextField(max_length=200, blank=False)
    body = models.TextField(blank=False)
    category = models.ForeignKey(Category, related_name="posts_category", on_delete=models.CASCADE, blank=False)
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft'
                            )
    class Meta:
        ordering = ['created_at']



class Comment(models.Model):
    contain = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['created_at']






#class Article_category(models.Model):
    #article = models.ManyToManyField(Article)
    #category = models.ManyToManyField(Category)



class Like(models.Model):
    # emoji = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)




class Article_tag(models.Model):
    article = models.ManyToManyField(Article)
    tag = models.ManyToManyField(Tag)