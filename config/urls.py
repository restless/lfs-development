from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

handler500 = 'lfs.core.views.server_error'

urlpatterns = [
    url(r'', include('lfs.core.urls')),
    url(r'^manage/', include('lfs.manage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    url(r'^reviews/', include('reviews.urls')),

    # Your stuff: custom urls go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
