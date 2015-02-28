from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yebitutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^centers/$', 'centers.views.centers', name='centers'),
    url(r'^center/new/$', 'centers.views.center_create', name='center_create'),
    url(r'^center/(?P<pk>\d+)/$', 'centers.views.center', name='center'),
    url(r'^center/(?P<pk>\d+)/edit/$', 'centers.views.center_update',\
        name='center_update'),
    url(r'^center/(?P<pk>\d+)/delete/$', 'centers.views.center_delete',\
        name='center_delete'),
)
