from django import forms

class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.Charfield(widget = forms.PasswordInput) #using the PasswordInput widget to render the password HTML element