from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    #LOGIN/REG URLS:
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),

    #BELT EXAM URLS:
    url(r'^add$', views.add_item),
    url(r'^create_item$', views.create_item),
    url(r'^wish_item/(?P<id>\d+)$', views.show_item),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish),
    url(r'^remove_wish/(?P<id>\d+)$', views.remove_wish),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]