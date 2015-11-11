from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /iterations/5/
    url(r'^(?P<iteration_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /iterations/5/start/
    url(r'^(?P<iteration_id>[0-9]+)/start/$', views.start, name='start'),
    # ex: /iterations/5/pause/
    url(r'^(?P<iteration_id>[0-9]+)/pause/$', views.pause, name='pause'),
    # ex: /iterations/5/end/
    url(r'^(?P<iteration_id>[0-9]+)/end/$', views.end, name='end'),

    # ex: /iterations/new/
    url(r'^new/$', views.new, name='new'),
    # ex: /iterations/create/
    url(r'^create/$', views.create, name='create'),
]