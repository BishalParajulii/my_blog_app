from . import views as v
from django.urls import path
from django.contrib.auth import views as auth_views# this is different from view.py


urlpatterns = [
    path('signup' , v.sign_up , name = 'users-sign-up'),
    path('login/' , auth_views.LoginView.as_view(template_name = 'users/login.html') , name = 'users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/' , v.profile, name = 'profile'),
]
