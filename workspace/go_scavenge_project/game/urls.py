from django.conf.urls import patterns, url
from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name ='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^gamescreen/$', views.gamescreen, name='gamescreen'),
	url(r'^gameover/$', views.gameover, name='gameover'),
    url(r'^loadgame/$', views.gamescreen, name='loadgame'),
)
