from django.conf.urls import url
from . import views

app_name = 'ufs'

urlpatterns =[
url(r'^messages/$',views.MessageCreateView.as_view(),name = 'ufs-messages'),
]
