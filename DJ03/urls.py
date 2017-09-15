from django.conf.urls import include, url
from django.contrib import admin

import notifications.urls

urlpatterns = [
    url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^giving/', include('giving.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('giving.urls')),
]
