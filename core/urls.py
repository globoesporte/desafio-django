
from django.urls import path
from .views import SurveyList,SurveyActs,OptionActs,VoteActs

urlpatterns = [
    path('api/vote/survey=<int:survey>/option=<int:pk>', VoteActs.as_view()),
    path('api/vote/survey=<int:survey>/old_option=<int:pkold>/new_option=<int:pk>', VoteActs.as_view()),
    path('api/options/', OptionActs.as_view()),
    path('api/options/survey=<int:survey>/option=<int:pk>', OptionActs.as_view()),
    path('api/surveys/', SurveyActs.as_view(),{'pk': None}),
    path('api/surveys/<int:pk>', SurveyActs.as_view()),
    path('surveys/', SurveyList),
    path('', SurveyList),


]
