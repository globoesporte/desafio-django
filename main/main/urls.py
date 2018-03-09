from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin


urlpatterns = [
	url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    # API
    url(r'^api/', include('api.urls')),

    # Main app urls
    url(r'^', include('polls.urls')),
] 
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)