from django.shortcuts import render
from .models import ExpertCorner
from django.views.generic import CreateView , ListView

class ExpertCornerCreateView(CreateView):
    model = ExpertCorner
    template_name = 'expertcorner/new.html'
    fields = ['Product','Technique_name','Description']
    success_url = '/shop/'
