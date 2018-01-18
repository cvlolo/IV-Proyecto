from django.conf.urls import patterns, url
from atpbot import views

urlpatterns = patterns('',
        url(r'^$', views.root, name='root'),
	url(r'^status', views.status, name='status'),
	url(r'^Clasificacion', views.Clasificacion, name='Clasificacion')

)
