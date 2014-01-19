from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from hd_app.views import IndexView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(u'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
        ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)