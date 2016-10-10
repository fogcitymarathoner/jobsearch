from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coltrane.models import Entry

entry_info_dict = {
            'queryset': Entry.objects.all(),
            'date_field': 'pub_date',
            }

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^search/$', 'search.views.search'),
    (r'^weblog/categories/',  include('coltrane.urls.categories')),
    (r'^weblog/links/',  include('coltrane.urls.links')),
    (r'^weblog/tags/',  include('coltrane.urls.tags')),
    (r'^weblog/',  include('coltrane.urls.entries')),
    (r'^tiny_mce/(?P<path>.*)$','django.views.static.serve',
         {'document_root': '/home/rocketsr/django_vendors/tiny_mce/'}),
    (r'', include('django.contrib.flatpages.urls')),

    (r'^envtest/$', 'search.views.envtest'),
)
