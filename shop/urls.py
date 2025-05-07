from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


app_name = 'shop'

urlpatterns = [

    path('shop/',login_required(TemplateView.as_view(template_name = 'shop/shop.html')) , name = 'shop'),
    path('shop/all_auctions/',views.AllAuctions.as_view() , name = 'all_auctions'),
    path('shop/auction/', views.AuctionCreateView.as_view(template_name = 'shop/auction.html') , name = 'created_auction'),
    path('shop/myauction/', views.MyAuctions.as_view(), name = 'myauctions'),
    re_path('shop/myauction/(?P<pk>[0-9]+)/', views.AuctionDetailView.as_view(), name = 'auction_detail'),
    # path('auction/')
    path('shop/services/',views.ServiceCreateView.as_view(), name = 'service'),
    path('shop/all_services/',views.ServiceListView.as_view(), name = 'all_services'),
    re_path('shop/service/(?P<pk>[0-9]+)/',views.ServiceDetailView.as_view(), name = 'service_detail'),
    path('shop/biddinglist/',views.BiddingList.as_view(),name = 'biddinglist'),
    re_path('shop/bidding/(?P<pk>[0-9]+)/',views.BiddingCreateView.as_view(),name = 'bidding')
]
