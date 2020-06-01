from django.db import models
import datetime as dt
from django.conf import settings
from django.contrib.auth.models import User

# add a field dynamicaly

                            

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


class Comment(models.Model):
    commentor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Image, on_delete=models.CASCADE)


class Follow(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL , related_name = 'rel_from_set' , on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL , related_name ='rel_to_set' ,on_delete=models.CASCADE)

User.add_to_class('following',
                  models.ManyToManyField('self',
                                        through=Follow,
                                        related_name='followers',
                                        symmetrical=False
                                        ))
                  
                 

