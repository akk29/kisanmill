from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm
from django.urls import path, resolve
from kisanmill.settings.base import LOGIN_URL


@login_required
def home(request):
    print(request.user)
    if request.user.is_authenticated():
        return render('/shop/')
    return render(request, 'core/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/shop/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def login_user(request):
    if not request.user.is_anonymous:
        return redirect('/shop/')
    return redirect('/log_in/')

def logout_user(request):
    if not request.user.is_anonymous:
        return redirect('/shop/')
    return redirect('/log_in/')

class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/login')
    

class MyLogoutView(LogoutView):
    """make logout available via GET"""
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def my_logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    # login_url = resolve(login_url or LOGIN_URL)
    return MyLogoutView.as_view(next_page='/log_in/')(request)