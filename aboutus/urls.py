from django.urls import path, include
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path('engineering', views.engineering, name='engineering'),
    path('equipmentinspection', views.equipmentinspection, name='equipmentinspection'),
    path('fabrication', views.fabrication, name='fabrication'),
    path('testing', views.testing, name='testing'),
]
