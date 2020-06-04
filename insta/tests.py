from django.test import TestCase
from .models import Profile,Comment,Image
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username ='Hamisi')
        self.new_profile = Profile(user = self.new_user)
        self.another_user = User.objects.create(username ='Salim')
        self.another_profile = Profile(user = self.another_user)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
        self.assertTrue(isinstance(self.new_user,User))

    def test_init(self):
        self.assertEqual(self.new_profile.bio,"Hello everyone amusing insta-clone")
        self.assertEqual(self.new_profile.user.username,"Hamisi")
        self.assertEqual(self.new_profile.photo,"../static/photos/profile.jpeg")

    def test_save_method(self):
        self.new_profile.save_profile()
        self.another_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 2)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.another_profile.save_profile()
        self.another_profile.delete_profile()

        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==1)

    def test_search_method(self):
        self.new_profile.save_profile()
        self.another_profile.save_profile()
        
        profiles = Profile.search_profile('z')
        self.assertEqual(len(profiles),0)

        profiles = Profile.search_profile('h')
        self.assertEqual(len(profiles),1)

    def test_get_profile(self):
        self.new_profile.save_profile()
        self.another_profile.save_profile()

        profile = Profile.get_profile(self.new_profile.id)
        self.assertTrue(profile is not None)

class ImageTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username ='Hamisi')
        self.new_profile = Profile.objects.create(user= self.new_user)
        self.new_image = Image(profile = self.new_profile , caption ="New caption")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_user,User))
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_image.save_image()
        
        images = Image.objects.all()
        self.assertTrue(len(images)== 1)

    def test_delete_method(self):
        self.new_image.save_image()

        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test__init(self):
        self.assertEqual(self.new_image.caption,"New caption")


    

        
    



        
       

