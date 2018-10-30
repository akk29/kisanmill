from django.conf.urls import url
from . import views

app_name = 'bond'

urlpatterns = [

    url(r'^bond/$',views.BondCreateView.as_view(),name = 'created_bond'),
    url(r'^bond/all$',views.BondListView.as_view(),name = 'all_bonds')

]
