from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .forms import loginForm,UserRegistratinForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

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


def dashboard(request):

    return render(request,'account/dashboard.html', {'section':'dashboard'})