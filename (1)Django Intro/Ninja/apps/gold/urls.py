from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^process_money$',views.money)
]
