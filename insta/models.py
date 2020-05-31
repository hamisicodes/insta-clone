from django.db import models
import datetime as dt
from django.conf import settings

# Create your models here.
class  Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #To refer the user model
    date_of_birth = models.DateField(blank =True, null =True)
    photo = models.ImageField(upload_to='users/' , blank=True)
    bio = models.TextField(default="Hello everyone amusing insta-clone")

    def __str__(self):
        return self.user.username


class Image(models.Model):
    name = models.CharField(max_length=50, blank=True) 
    image = models.ImageField(upload_to='posts', blank=True)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
