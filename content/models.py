from django.db import models

from account.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE,blank = True)
    content = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = "post",null = True)
    saved_user = models.ManyToManyField(User,related_name = "saved_posts",null = True,blank = True)
    created_at = models.DateTimeField(auto_now_add = True,blank = True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
