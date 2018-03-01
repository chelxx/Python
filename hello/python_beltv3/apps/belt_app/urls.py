from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    #LOGIN/REG URLS HERE:
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^success$', views.success),

    #BELT EXAM URLS HERE:
    url(r'^add_form$', views.add_form),
    url(r'^add_trip$', views.add_trip),
    url(r'^my_trip/(?P<id>\d+)$', views.my_trip),
    url(r'^remove_my_trip/(?P<id>\d+)$', views.remove_my_trip),
    url(r'^show_trip/(?P<id>\d+)$', views.show_trip),  
    url(r'^delete/(?P<id>\d+)$', views.delete),
]