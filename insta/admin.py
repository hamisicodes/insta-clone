from django.contrib import admin
from .models import Profile,Image

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_of_birth', 'photo','bio')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display =('image','name','caption')

