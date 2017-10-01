from django.conf.urls import *

from news_sitemaps import registry
from .views import *

urlpatterns = [
    url(r'^index\.xml$',
        index,
        {'sitemaps': registry},
        name='news_sitemaps_index'),

    url(r'^(?P<section>.+)\.xml',
        news_sitemap,
        {'sitemaps': registry},
        name='news_sitemaps_sitemap'),
]
