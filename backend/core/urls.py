from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.home, name='home'),
    path('login', core_views.login_user,name='login'),

    path('log_in/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout', core_views.my_logout_then_login, name='logout'),
    
    path('signup', core_views.signup, name='signup'),
]
