from django.urls import path, re_path
from . import views

app_name = 'administrator'


urlpatterns  = [

    path('administrator/',views.adminhome , name = 'admin'),
    path('administrator/messages/',views.MessageListView.as_view() , name = 'messagelist'),
    re_path('administrator/messages/(?P<pk>[0-9]+)/', views.MessageDetailView.as_view() , name = 'messagedetail'),

]
