from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('core.urls')),
    path(r'^admin/', admin.site.urls),
]
