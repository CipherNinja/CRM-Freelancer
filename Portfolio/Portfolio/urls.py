from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('freelancer.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
