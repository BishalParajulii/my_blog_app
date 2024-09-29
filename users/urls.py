from . import views
from django.urls import path
from django.contrib.auth import views as vw # this is different from view.py


urlpatterns = [
    path('signup' , views.sign_up , name = 'users-sign-up'),
    path('login/' , vw.LoginView.as_view(template_name = 'users/login.html') , name = 'users-login'),
    path('logout/' , vw.LogoutView.as_view(template_name = 'users/logout.html') , name = 'users-logout'),
]
