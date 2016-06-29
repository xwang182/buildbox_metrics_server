from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^metrics/api/v1.0/', include('buildbox_metrics.urls')),
    url(r'^admin/', admin.site.urls),
]
