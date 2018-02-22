from django.conf.urls import url
from . import views

#ITTY BITTY URLS - they go AFTER BIG URL, they also connect to your VIEWS.
urlpatterns = [
    url(r'^$', views.index), #localhost:8000/ 
    url(r'^new$', views.new), #localhost:8000/new
    url(r'^(?P<id>\d+)/edit$', views.edit), #localhost:8000/<id>/edit
    url(r'^(?P<id>\d+)/show$', views.show), #localhost:8000/<id>/show
    url(r'^create$', views.create), #localhost:8000/create
    url(r'^(?P<id>\d+)/destroy$', views.destroy), #localhost:8000/<id>/destroy
    url(r'^(?P<id>\d+)/update$', views.update), #localhost:8000/update
]