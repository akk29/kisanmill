from django.urls import path , include
from . import views

app_name = 'accounts'

urlpatterns = [
    path(r'accounts/profile/$',views.profile,name = 'profile'),
    path(r'accounts/products/$',views.Myproducts.as_view(),name = 'update-products'),

]
