from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^golfers$', views.golfer_list, name='golfer_list')
]
