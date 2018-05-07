from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$',views.survey),
	url(r'^result$', views.result),
	url(r'^return$', views.goback)
]