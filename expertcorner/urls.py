from django.urls import path
from . import views
app_name = 'expertcorner'

urlpatterns = [

    path('suggest/',views.ExpertCornerCreateView.as_view(),name = 'suggest'),

]
