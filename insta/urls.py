from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.dashboard , name = 'dashboard'),
    # path('login/' , views.user_login , name = 'login')
    path('' , auth_views.LoginView.as_view() ,name ='login'),
    path('logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),

]


