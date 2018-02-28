from django.urls import path, include
from .views import SurveyList

urlpatterns = [
    path('survey/', SurveyList.as_view()),
]
