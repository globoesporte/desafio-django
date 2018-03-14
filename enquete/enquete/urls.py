"""enquete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # enquete
    url(r'^enquete/$', views.EnqueteList.as_view(), name='enquete-list'),
    url(r'^enquete/(?P<pk>[0-9]+)/$', views.EnqueteDetail.as_view(), name='enquete-detail'),
    url(r'^enquete/edit/(?P<pk>[0-9]+)/$', views.EnqueteEditView.as_view(), name='enquete-edit'),
    url(r'^enquete/all/', views.EnqueteListView.as_view(), name='enquete-all'),
    url(r'^enquete/new/', views.EnqueteNewView.as_view(), name='enquete-new'),
    
    # item
    url(r'^item/$', views.ItemList.as_view(), name='item-list'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view(), name='item-detail'),
    url(r'^item/edit/(?P<pk>[0-9]+)/$', views.ItemEditView.as_view(), name='item-edit'),
    url(r'^item/all/', views.ItemListView.as_view(), name='item-all'),
    url(r'^item/new/', views.ItemNewView.as_view(), name='item-new'),
    
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]

 
# urlpatterns = format_suffix_patterns(urlpatterns)