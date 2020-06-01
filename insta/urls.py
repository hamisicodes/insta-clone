from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard , name = 'dashboard'),
    path('register/', views.register, name='register'),
    path('login/' , auth_views.LoginView.as_view() ,name ='login'),
    path('logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),
    path('edit/', views.edit , name='edit'),
    path('create/', views.create , name='create'),
    path('profile/', views.profile, name= 'profile'),
    path('profile/<username>', views.get_profile, name= 'get_profile'),
    path('comment/<int:pk>', views.comment , name= 'comment'),
    path('follow/<int:user_to>', views.follow , name= 'follow')
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


