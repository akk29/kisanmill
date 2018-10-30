from django.conf.urls import url , include
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'accounts/profile/$',views.profile,name = 'profile'),
    url(r'accounts/products/$',views.Myproducts.as_view(),name = 'update-products'),

]
