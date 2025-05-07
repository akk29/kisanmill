from django.urls import path , include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'),name='index'),
    path('admin', admin.site.urls),
    path('about', TemplateView.as_view(template_name = 'about1.html'),name='about'),

    #customer corner

    path('',include('customercorner.urls')),
    path('',include('core.urls')),
    path('',include('accounts.urls')),
    path('',include('ufs.urls')),
    path('',include('administrator.urls')),
    path('',include('shop.urls'))   ,
    path('',include('bond.urls')),
    path('',include('expertcorner.urls'))
]

