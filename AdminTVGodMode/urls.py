from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/', include('website.urls')),
    path('api/', include('inspections.urls')),
    path('api/', include('marketplace.urls')),
    path('api/admin/', include('admin_api.urls')),
    path('api/', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
