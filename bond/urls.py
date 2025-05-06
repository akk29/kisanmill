from django.urls import path
from . import views

app_name = 'bond'

urlpatterns = [

    path('bond',views.BondCreateView.as_view(),name = 'created_bond'),
    path('bond/all',views.BondListView.as_view(),name = 'all_bonds')

]
