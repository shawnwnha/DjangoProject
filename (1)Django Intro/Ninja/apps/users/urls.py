from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.user),
    url(r'^login$', views.login),
    url(r'^users/new$', views.user),
    url(r'^users$', views.users),

]