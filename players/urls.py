__author__ = 'derekchiu'

from django.conf.urls import patterns, url

import players.views as stats_views

urlpatterns = patterns('players.stats_views',
    url(r'^$', stats_views.enterName, name='home'),
    url(r'^stats', stats_views.getstats, name='stats')
)
