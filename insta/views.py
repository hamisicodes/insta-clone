from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .forms import loginForm,UserRegistratinForm,UserEditForm,ProfileEditForm,ImageForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Profile,Image
from  django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistratinForm(request.POST)
        
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit= False)
            # set the chose password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the new user
            new_user.save()
            Profile.objects.create(user= new_user)
            messages.success(request ,'Account created successfully')
            return redirect('login')



    else:
        user_form = UserRegistratinForm()

        return render(request,'account/register.html' , {'user_form':user_form})



@login_required
def dashboard(request):
    posts = Image.objects.all()


    return render(request,'account/dashboard.html', {'posts':posts})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form =UserEditForm(instance=request.user , data=request.POST)
        profile_form =ProfileEditForm(instance = request.user.profile, data =request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request ,'Profie updated successfully')
        
        else:
            messages.error(request,'Error updating profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form':user_form , 'profile_form':profile_form})


def create(request):
    if request.method == 'POST:
        image_form = ImageForm(request.POST,request.FILES)
        profile = Profile.objects.get(id = request.user.id)

        if image_form.is_valid():
            post = image_form.save(commit = False)
            post.profile = profile
            post.save()

            messages.success(request ,'New Post added successfully')
            return redirect('dashboard')

    else:
        image_form= ImageForm()
        return render(request,'account/post.html', {'image_form':image_form})