from django import forms
from django.contrib.auth.models import User
from .models import Profile,Image

class ImageForm(forms.ModelForm):
    class Meta:
        model =Image
        fields = ('image','caption')



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo','bio')

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput) #using the PasswordInput widget to render the password HTML element

class UserRegistratinForm(forms.ModelForm):
    password = forms.CharField(label ='Password',
                                widget = forms.PasswordInput)

    password2 =forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'email')    
    
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords dont match')
    
        return cd['password2']
            