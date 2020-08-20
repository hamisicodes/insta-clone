from django.db import models
import datetime as dt
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime as dt

# add a field dynamicaly

                            

# Create your models here.
class  Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #To refer the user model
    date_of_birth = models.DateField(blank =True, null =True)
    photo = models.ImageField(upload_to='users/' , blank=True , default='../static/photos/profile.jpeg')
    bio = models.TextField(default="Hello everyone amusing insta-clone")

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

    @classmethod
    def search_profile(cls,name):
        profile = cls.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_profile(cls,id):
        profile = cls.objects.get(id = id)
        return profile
    

class Image(models.Model):

    name = models.CharField(max_length=50, blank=True) 
    image = models.ImageField(upload_to='posts', blank=True)
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='likes' , blank =True) #likes
    created_at =models.DateTimeField(auto_now_add=True,blank=True,null =True)
    

    class Meta:
        ordering = ['-pk']

    def save_image(self):
        self.save()
        

    def delete_image(self):
        self.delete()

    def all_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.name

    @classmethod
    def update_caption(cls,pk,caption_update):
        image = cls.objects.get(pk = pk)
        image.update(caption = caption_update)

    @classmethod
    def get_image(cls,id):
        image = cls.objects.get(id = id)
        return image





class Comment(models.Model):
    commentor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Image, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
        

    def delete_comment(self):
        self.delete()

      
        
class Follow(models.Model):
    user_from = models.ForeignKey(User , related_name = 'rel_from_set' , on_delete=models.CASCADE)
    user_to = models.ForeignKey(User , related_name ='rel_to_set' ,on_delete=models.CASCADE)

User.add_to_class('following',
                  models.ManyToManyField('self',
                                        through=Follow,
                                        related_name='followers',
                                        symmetrical=False
                                        ))
                  
                 

