from django.urls import path
from .views import SurveyPrivate, OptionPublic

urlpatterns = [
     # lista todas as enquetes (GET) OU cria uma nova enquete (POST)
     path('survey/', SurveyPrivate.as_view(), {'pk': None}),
     # Mostra uma enquete específica (GET), modifica uma enquete (PUT), remove uma enquete (DELETE)
     path('survey/<int:pk>', SurveyPrivate.as_view()),
     path('option/', OptionPublic.as_view())

]
