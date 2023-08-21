from django.contrib import admin
from django.urls import path, include

from .api import api

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('crm/', include('backend.crm.urls', namespace='crm')),
    path('api/v1/', api.urls),
    path('admin/', admin.site.urls),
]
