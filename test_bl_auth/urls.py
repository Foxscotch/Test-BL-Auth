from django.conf.urls import patterns, url

from test_bl_auth import views

urlpatterns= patterns('',
    url(r'^$', views.get_id, name='index'),
    url(r'result', views.give_id, name='result')
)
