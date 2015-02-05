from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^problem/', include('problem.urls')),
    url(r'^get_time/', 'index.views.get_time'),
    url(r'^index/', include('index.urls', namespace='index')),
    url(r'^contest/', include('contest.urls', namespace='contest')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^team/', include('team.urls', namespace='team')),
    url(r'^group/', include('group.urls', namespace='group')),
    url(r'^status/', include('status.urls', namespace='status')),
    url(r'^broken/', 'index.views.broken'),
)
