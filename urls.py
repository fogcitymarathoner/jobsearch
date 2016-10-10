from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from coltrane.models import Entry
"""
from coltrane.feeds import CategoryFeed, LatestEntriesFeed

feeds = { 'entries': LatestEntriesFeed,
          'categories': CategoryFeed }
"""


entry_info_dict = {
            'queryset': Entry.objects.all(),
            'date_field': 'pub_date',
            }
urlpatterns = patterns('django.views.generic.simple',
    ('^$', 'redirect_to', {'url': '/home/'}, 'home'),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
urlpatterns += patterns('',
    (r'^auth/login/', 'login.views.loginView'),          
    (r'^auth/logout/', 'login.views.logoutView'),   
    (r'^admin/', include(admin.site.urls)),
    (r'^search/$', 'search.views.search'),
    (r'^comments/', include('django.contrib.comments.urls')),
    #(r'^weblog/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }),
    (r'^weblog/categories/',  include('coltrane.urls.categories')),
    (r'^weblog/links/',  include('coltrane.urls.links')),
    (r'^weblog/tags/',  include('coltrane.urls.tags')),
    (r'^weblog/',  include('coltrane.urls.entries')),
    #(r'^schedule/',  include('schedule.urls')),
    #(r'^todo/',  include('todo.urls')),
    (r'^fckeditor/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.VENDOR_ROOT+'fckeditor/'}),
    (r'', include('django.contrib.flatpages.urls')),

    (r'^envtest/$', 'search.views.envtest'),
)

