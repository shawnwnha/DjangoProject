from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$',views.loginpage),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^books$', views.main),
	url(r'^books/add$', views.addpage),
	url(r'^books/add/process$', views.add),
	url(r'^books/(?P<book_id>\d+)$', views.show),
	url(r'^review$', views.review),
	url(r'^users/(?P<user_id>\d+)$', views.user),
]