from django.urls import path, include
from . import views
from django.conf import settings
from django.views import defaults as default_views

urlpatterns = [
    path('clientprojects', views.clientprojects, name='clientprojects'),
    path('equipmentdetail', views.equipmentdetail, name='equipmentdetail'),
    path('equipmentimages', views.equipmentimages, name='equipmentimages'),
    path('equipmentlist', views.equipmentlist, name='equipmentlist'),
]