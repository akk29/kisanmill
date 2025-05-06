from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


app_name = 'shop'

urlpatterns = [

    path(r'^shop/$',login_required(TemplateView.as_view(template_name = 'shop/shop.html')) , name = 'shop'),
    path(r'^shop/all_auctions/$',views.AllAuctions.as_view() , name = 'all_auctions'),
    path(r'^shop/auction/$', views.AuctionCreateView.as_view(template_name = 'shop/auction.html') , name = 'created_auction'),
    path(r'^shop/myauction/$', views.MyAuctions.as_view(), name = 'myauctions'),
    path(r'^shop/myauction/(?P<pk>[0-9]+)/$', views.AuctionDetailView.as_view(), name = 'auction_detail'),
    # path(r'^auction/$')
    path(r'^shop/services/$',views.ServiceCreateView.as_view(), name = 'service'),
    path(r'^shop/all_services/$',views.ServiceListView.as_view(), name = 'all_services'),
    path(r'^shop/service/(?P<pk>[0-9]+)/$',views.ServiceDetailView.as_view(), name = 'service_detail'),
    path(r'^shop/biddinglist/',views.BiddingList.as_view(),name = 'biddinglist'),
    path(r'^shop/bidding/(?P<pk>[0-9]+)/$',views.BiddingCreateView.as_view(),name = 'bidding')
]
