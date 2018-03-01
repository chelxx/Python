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
    # url(r'^ ** $', views. ** ),
    # url(r'^ ** /(?P<id>\d+)$', views. ** ),
]