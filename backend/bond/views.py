from django.shortcuts import render , render , redirect
from .models import Bond
from django.views.generic import CreateView , ListView


class BondCreateView(CreateView):
    model = Bond
    fields = ['name','investment_amount','expectations','facilities']
    template_name = 'bond/create_bond.html'
    context_object_name = 'form'
    success_url = '/shop'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return redirect('/shop/')

class BondListView(ListView):
    model = Bond
    template_name = 'bond/all_bonds.html'
    context_object_name = 'all_bond'
