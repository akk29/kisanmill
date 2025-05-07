from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/profile/',views.profile,name = 'profile'),
    path('accounts/products',views.Myproducts.as_view(),name = 'update-products'),
]
