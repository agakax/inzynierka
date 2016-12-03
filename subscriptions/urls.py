from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^photos/', views.photos_list, name='photos_list'),
    url(r'^photos/([a-zA-Z]+)/image=([0-9]+)/', views.photo_big, name='photo_big'),
    url(r'^photos/([a-zA-Z]+)/image=([0-9]+)/send/', views.send_photo, name='send_photo'),
    url(r'^subs/list/', views.subs_list, name='subs_list'),
    url(r'^subs/new/', views.subs_new, name='subs_new'),
    url(r'^subs/edit=([0-9]+)/', views.subs_edit, name='subs_edit'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]