from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard/', views.dashboard , name = 'dashboard'),
    path('register/', views.register, name='register'),
    path('' , auth_views.LoginView.as_view() ,name ='login'),
    path('logout/' , auth_views.LogoutView.as_view(),{"next_page": '/'} ,name ='logout' ),
    path('edit/', views.edit , name='edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


