from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    #URLS for Login/Reg
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    
    #URLS for Courses
    url(r'^create$', views.create),
    url(r'^edit/(?P<id>\d+)/$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^delete/destroy/(?P<id>\d+)$', views.destroy), 
    url(r'^favorite/(?P<id>\d+)$', views.favorite),
    url(r'^unfavorite/(?P<id>\d+)$', views.unfavorite), 
]