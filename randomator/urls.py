from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.haml"), name='home'),
    url(r'^inspiration/', include('inspiration.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
