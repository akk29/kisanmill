from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .forms import MyproductsForm
from .models import Myproducts

@login_required
def profile(request):
    # form = ProfileForm()
    return redirect('/shop/')

class Myproducts(UpdateView,LoginRequiredMixin):
    
    form_class = MyproductsForm
    template_name = 'accounts/Myproducts.html'

    def get_queryset(self):
        return Myproducts.objects.get(pk = self.request.user)
