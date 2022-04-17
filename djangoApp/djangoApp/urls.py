from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoApp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tableApp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'tableApp.views.view_404'