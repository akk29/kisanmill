from django.conf.urls import url
from . import views

app_name = 'administrator'


urlpatterns  = [

    url(r'^administrator/$',views.adminhome , name = 'admin'),
    url(r'^administrator/messages/$',views.MessageListView.as_view() , name = 'messagelist'),
    url(r'^administrator/messages/(?P<pk>[0-9]+)/$', views.MessageDetailView.as_view() , name = 'messagedetail'),

]
