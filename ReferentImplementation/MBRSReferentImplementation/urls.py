from django.conf.urls import patterns, include, url
from django.contrib import admin
from MBRSReferentImplementation.forms import DetailUser

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'MBRSReferentImplementation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('states.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^udetail/(?P<pk>\d+)/$', DetailUser.as_view(), name='udetail'),
)
