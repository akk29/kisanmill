from django.urls import path
from . import views

app_name = 'ufs'

urlpatterns =[
path('messages/',views.MessageCreateView.as_view(),name = 'ufs-messages'),
]
