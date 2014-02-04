from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from paste.models import Paste

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'paste.views.home', name='home'),
	url(r'^paste/(?P<pk>\d+)$', DetailView.as_view(model=Paste,
									context_object_name='paste',
									template_name='paste.html'
									), name='paste'),
	url(r'^repaire/(?P<pk>\d+)$', 'paste.views.home', name='repaire'),
	url(r'^delete/(?P<pk>\d+)$', DeleteView.as_view(model=Paste,
									success_url='/',
									template_name='item_confirm_delete.html'
									), name='delete'),
	url(r'^admin/', include(admin.site.urls)),
	(r'^i18n/', include('django.conf.urls.i18n')),
)
