from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from django.conf.urls import url

router = routers.SimpleRouter()

router.register(r'options', views.OptionViewSet)
router.register(r'polls', views.PollViewSet)
router.register(r'vote', views.VoteViewSet)

urlpatterns = router.urls

urlpatterns += [
	url(r'docs', include_docs_urls(title='Globo Esporte API', public=False))
]