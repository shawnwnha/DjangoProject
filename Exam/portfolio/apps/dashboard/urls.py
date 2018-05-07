from django.conf.urls import url
from . import views 

urlpatterns =[
	url(r'^$', views.welcomepage),
	url(r'^login$', views.loginpage),
	url(r'^login/0$', views.login),
	url(r'^register$', views.registerpage),
	url(r'^register/0$', views.register),
	url(r'^dashboard$', views.dashboard),
	url(r'^dashboard/admin$', views.adminboard),
	url(r'^user/show/(?P<id>\d+)$', views.show)
]