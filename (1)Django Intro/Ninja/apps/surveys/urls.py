from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.first),
    url(r'^/new$', views.second )
]
