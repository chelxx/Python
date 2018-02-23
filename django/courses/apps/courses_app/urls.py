from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    
    url(r'^create/$', views.create),
    url(r'^destroy/(?P<id>\d+)$', views.destroy), 
    # url(r'^delete/$', views.delete), 
   
 
]


# {% url "courses":"index" %}


# render redirect (reverse("courses":"index")

# render (request, "course_a/index")