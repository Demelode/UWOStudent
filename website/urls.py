from django.conf.urls import patterns, url, include
from website import views

urlpatterns = patterns('website.views',
    url(r'^$', views.main, name='main'),
    url(r'main', views.main, name='main'),
    url(r'user', views.user, name='user'),
    url(r'login', views.login, name='login')
)
