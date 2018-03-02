from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin


urlpatterns = [
	url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    # my apps
    url(r'^api/', include('polls.urls')),
]