from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^$',views.main),
	url(r'^buy$',views.order),
	url(r'^checkout$', views.checkout)
]