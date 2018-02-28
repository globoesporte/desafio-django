from django.urls import path
from .views import SurveyList, SurveyInfo

urlpatterns = [
    path('survey/', SurveyList.as_view()),
    path('survey/<int:pk>', SurveyInfo.as_view()),

]
