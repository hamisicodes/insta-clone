from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .forms import loginForm,UserRegistratinForm,UserEditForm,ProfileEditForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Profile
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

            return redirect('login')



    else:
        user_form = UserRegistratinForm()
        return render(request,'account/register.html' , {'user_form':user_form})


    












def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username =  cd['username'],
                                password =  cd['password']
                                 )    
            if user is not None:
                if user.is_active:
                    login(request ,user)
                    return HttpResponse('Authenticated Successfully')

                else:
                    return HttpResponse('Account disabled')

            
            else:
                return HttpResponse('Invalid Login')


    else:
        form = loginForm()
    
    return render(request , 'account/login.html' , {'form':form})


@login_required
def dashboard(request):
    return render(request,'account/dashboard.html', {'section':'dashboard'})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form =UserEditForm(instance=request.user , data=request.POST)
        profile_form =ProfileEditForm(instance = request.user.profile, data =request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form':user_form , 'profile_form':profile_form})
