from django.conf import settings
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls

from base import views as base_views

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),

    url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/v1/getdata/', include('base.urls', namespace='base')),

    url(r'', include(wagtail_urls)),
]
