from django.urls import path
from . import views

app_name = 'administrator'


urlpatterns  = [

    path(r'^administrator/$',views.adminhome , name = 'admin'),
    path(r'^administrator/messages/$',views.MessageListView.as_view() , name = 'messagelist'),
    path(r'^administrator/messages/(?P<pk>[0-9]+)/$', views.MessageDetailView.as_view() , name = 'messagedetail'),

]
