from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('peak/', include('peak.urls')),
]
