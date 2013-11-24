from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from unicorns.views import homepage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unicornssay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', homepage),

    # url(r'^admin/', include(admin.site.urls)),
)
