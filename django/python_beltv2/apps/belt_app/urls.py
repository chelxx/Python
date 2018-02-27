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
    # url(r'^ ** $', views. **),
    # url(r'^ ** /(?P<id>\d+)$', views. ** ),
]