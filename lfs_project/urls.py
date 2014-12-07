from django.conf.urls import patterns, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

handler500 = 'lfs.core.views.server_error'

urlpatterns = patterns("",
    (r'', include('lfs.core.urls')),
    (r'^manage/', include('lfs.manage.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^reviews/', include('reviews.urls')),

    # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


