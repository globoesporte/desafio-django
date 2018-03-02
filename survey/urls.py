from django.urls import path
from .views import SurveyPrivate, OptionPublic, OptionPrivate

urlpatterns = [
     # lista todas as enquetes (GET) OU cria uma nova enquete (POST)
     path('survey/', SurveyPrivate.as_view(), {'pk': None}),
     # Mostra uma enquete específica (GET), modifica uma enquete (PUT), remove uma enquete (DELETE)
     path('survey/<int:pk>', SurveyPrivate.as_view()),
     # faz um unico voto (POST)
     path('vote/', OptionPublic.as_view()),
     # Modifica uma opção (PUT)
     path('option/<int:pk>', OptionPrivate.as_view()),
     # Cria uma nova opção (POST)
     path('option/', OptionPrivate.as_view())

]
