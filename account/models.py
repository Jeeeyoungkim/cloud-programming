from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to = "user",default = "/user/default.png")
    nickname = models.CharField(max_length = 100)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers',null = True)
    introduction = models.CharField(max_length = 500,null = True, blank = True)
    is_sad = models.ManyToManyField("content.Post",null = True, blank = True, related_name = "sad_users")
