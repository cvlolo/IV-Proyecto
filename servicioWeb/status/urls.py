from django.conf.urls import patterns, url
from status import views

urlpatterns = patterns('',
        url(r'^$', views.root, name='root')

)
