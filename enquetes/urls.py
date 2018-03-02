from django.urls import path

from . import views

from django.conf.urls import url, include

from rest_framework_nested import routers


resposta_router = routers.DefaultRouter()
resposta_router.register(r'resposta', views.RespostaViewSet)
# ENDPOINTs partindo de 'resposta'
resposta_nested_router = routers.NestedSimpleRouter(
    resposta_router, r'resposta', lookup='resposta')
resposta_nested_router.register(r'voto', views.VotoViewSet,
                                base_name='resposta-voto')

enquete_router = routers.DefaultRouter()
enquete_router.register(r'enquete', views.EnqueteViewSet)
# ENDPOINTs partindo de 'enquete'
enquete_nested_router = routers.NestedSimpleRouter(
    enquete_router, r'enquete', lookup='enquete')
enquete_nested_router.register(r'respostas', views.RespostasViewSet,
                               base_name='enquete-respostas')


app_name = 'enquetes'

urlpatterns = [
    # API de enquete
    url(r'^api/', include(enquete_router.urls)),
    url(r'^api/', include(enquete_nested_router.urls)),
    # API de resposta
    url(r'^api/', include(resposta_router.urls)),
    url(r'^api/', include(resposta_nested_router.urls)),
    # Browser Version REST
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # Django web view URLS
    path('', views.IndexView.as_view(), name='index'),
    path('<int:enquete_id>/votar/', views.votar, name='votar'),
]
