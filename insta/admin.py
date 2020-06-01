from django.contrib import admin
from .models import Profile,Image,Comment

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_of_birth', 'photo','bio')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display =('image','name','caption')

@admin.register(Comment)
class ImageAdmin(admin.ModelAdmin):
    list_display =('commentor','comment','post')

