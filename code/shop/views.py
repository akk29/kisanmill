from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView , ListView
from .models import Auction , Services , Bidding
from .forms import ServiceCreateForm

class AuctionCreateView(LoginRequiredMixin,CreateView):
    model = Auction
    fields = ['Product','Price','Quality','Description','Min_order','Address','image']
    context_object_name = 'form'
    success_url = '/shop/myauction'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return redirect('/shop/myauction')


class AllAuctions(ListView):
    model = Auction
    context_object_name = 'AllAuctions'
    template_name = 'shop/all_auctions.html'


class MyAuctions(ListView):
    template_name = 'shop/myauction.html'
    context_object_name = 'data'

    def get_queryset(self):
        data = Auction.objects.all().filter(created_by = self.request.user)
        return data

class AuctionDetailView(DetailView):
    model = Auction
    template_name = 'shop/auction_detail.html'
    context_object_name = 'Auction_Detail'

class ServiceCreateView(LoginRequiredMixin,CreateView):
    model = Services
    form_class = ServiceCreateForm
    template_name = 'shop/services.html'
    success_url = '/shop/services'

class ServiceListView(ListView):
    model = Services
    template_name = 'shop/all_services.html'
    context_object_name = 'All_services'

class ServiceDetailView(DetailView):
    model = Services
    template_name = 'shop/service_detail.html'
    context_object_name = 'service_detail'


class BiddingList(ListView):
    model = Auction
    context_object_name = 'AllAuctions'
    template_name = 'shop/all_bid_auction.html'


class BiddingCreateView(LoginRequiredMixin,CreateView):
    model = Bidding
    fields = ['Bidding_Price','sample','Query']
    template_name = 'shop/bidding.html'
    context_object_name = 'data'

    def get_context_data(self,**kwargs):
        context = super(BiddingCreateView,self).get_context_data(**kwargs)
        context['data'] = Auction.objects.get(pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.bid_by = self.request.user
        # print self.kwargs['pk']
        a = Auction.objects.get(pk = self.kwargs['pk'])
        print a
        obj.Auction = a
        obj.save()
        return redirect('/shop/myauction')
