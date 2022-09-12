from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('clientdetails', views.clientdetails, name='clientdetails'),
    path('userdetails', views.personview.as_view(), name='userdetails'),
    path('clienthome', views.clienthome, name='clienthome'),
    path('person/', views.PersonViewSet.list(), name='person'),
    path('person/new/', views.PersonViewSet.create(), name='new-person'),
    path('person/<int:pk>/edit/', views.PersonViewSet.update(), name='edit-person'),
    path('person/<int:pk>/delete2/', views.PersonViewSet.delete(), name='delete-person'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('person/<int:pk>/update/', views.person_update, name='person_update'),
    path('person/create/', views.person_create, name='person_create'),
    path('personlist', views.person_list, name='person_list'),
]