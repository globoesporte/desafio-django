from . import views
from rest_framework import routers


router = routers.SimpleRouter()

router.register(r'options', views.OptionViewSet)
router.register(r'polls', views.PollViewSet)
router.register(r'vote', views.VoteViewSet)

urlpatterns = router.urls