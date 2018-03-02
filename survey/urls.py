from django.urls import path
from .views import SurveyInfo, OptionInfo

urlpatterns = [
     # lista todas as enquetes (GET) OU cria uma nova enquete (POST)
     path('survey/', SurveyInfo.as_view(), {'pk': None}),
     # Mostra uma enquete específica (GET), modifica uma enquete (PUT), remove uma enquete (DELETE)
     path('survey/<int:pk>', SurveyInfo.as_view()),
     path('option/', OptionInfo.as_view())

]
