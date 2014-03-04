from django.conf.urls import patterns, url
from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
)
