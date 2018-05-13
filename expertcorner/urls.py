from django.conf.urls import url
from . import views
app_name = 'expertcorner'

urlpatterns = [

    url(r'^suggest/$',views.ExpertCornerCreateView.as_view(),name = 'suggest'),

]
