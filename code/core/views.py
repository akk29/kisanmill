from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SignUpForm


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
