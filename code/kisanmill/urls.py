from django.conf.urls import url , include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'index.html'),name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'),name='about'),

    #customer corner

    url(r'^',include('customercorner.urls')),
    url(r'^',include('core.urls')),
    url(r'^',include('accounts.urls')),
    url(r'^',include('ufs.urls')),
    url(r'^',include('administrator.urls')),
    url(r'^',include('shop.urls'))   ,
    url(r'^',include('bond.urls')),
    url(r'^',include('expertcorner.urls'))


]
