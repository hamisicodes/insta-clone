from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .forms import loginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

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