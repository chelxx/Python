from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),

    url(r'^add$', views.add),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]