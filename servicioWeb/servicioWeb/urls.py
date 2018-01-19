from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^atpbot/', include('atpbot.urls')),
    url(r'^status/', include('status.urls')),
)
