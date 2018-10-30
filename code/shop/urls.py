from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


app_name = 'shop'

urlpatterns = [

    url(r'^shop/$',login_required(TemplateView.as_view(template_name = 'shop/shop.html')) , name = 'shop'),
    url(r'^shop/all_auctions/$',views.AllAuctions.as_view() , name = 'all_auctions'),
    url(r'^shop/auction/$', views.AuctionCreateView.as_view(template_name = 'shop/auction.html') , name = 'created_auction'),
    url(r'^shop/myauction/$', views.MyAuctions.as_view(), name = 'myauctions'),
    url(r'^shop/myauction/(?P<pk>[0-9]+)/$', views.AuctionDetailView.as_view(), name = 'auction_detail'),
    # url(r'^auction/$')
    url(r'^shop/services/$',views.ServiceCreateView.as_view(), name = 'service'),
    url(r'^shop/all_services/$',views.ServiceListView.as_view(), name = 'all_services'),
    url(r'^shop/service/(?P<pk>[0-9]+)/$',views.ServiceDetailView.as_view(), name = 'service_detail'),
    url(r'^shop/biddinglist/',views.BiddingList.as_view(),name = 'biddinglist'),
    url(r'^shop/bidding/(?P<pk>[0-9]+)/$',views.BiddingCreateView.as_view(),name = 'bidding')
]
