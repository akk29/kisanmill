from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views as customercorner

app_name = 'customercorner'

urlpatterns = [

    path('all_products/' , customercorner.AllProductList.as_view() , name ='products' ),
    re_path('product_details/(?P<pk>[0-9]+)/' , customercorner.ProductDetailView.as_view() , name ='product_detail' ),
    path('create_product/',customercorner.ProductCreateView.as_view(),name='create_product'),
    path('categories/',customercorner.Categories.as_view(),name='categories'),
    re_path('categories/(?P<pk>[0-9]+)/',customercorner.category_products_list ,name='category_products')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
