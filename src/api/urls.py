from django.conf.urls import url
from django.urls import path

from .views import AllQuestionsView, QuestionView, ChoiceView, AllChoicesView, VoteView

app_name = 'api'

urlpatterns = [
    path('', AllQuestionsView.as_view(), name='allquestions'),
    path('<int:pk>', QuestionView.as_view(), name='question'),
    path('choices', AllChoicesView.as_view(), name='choices'),
    path('choices/<int:pk>', ChoiceView.as_view(), name='choice'),
    path('choices/vote/<int:pk>', VoteView.as_view(), name='vote'),
]
