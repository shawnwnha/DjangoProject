from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.main),
    url(r'^add$',views.add),
    url(r'^course/destroy/(?P<id>\d+)$',views.deletepage),
    url(r'^course/destroy/(?P<id>\d+)/delete$',views.delete)
]
