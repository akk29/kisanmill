from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views as customercorner

app_name = 'customercorner'

urlpatterns = [

    url(r'^all_products/$' , customercorner.AllProductList.as_view() , name ='products' ),
    url(r'^product_details/(?P<pk>[0-9]+)/$' , customercorner.ProductDetailView.as_view() , name ='product_detail' ),
    url(r'^create_product/$',customercorner.ProductCreateView.as_view(),name='create_product'),
    url(r'^categories/$',customercorner.Categories.as_view(),name='categories'),
    url(r'^categories/(?P<pk>[0-9]+)/$',customercorner.category_products_list ,name='category_products')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
