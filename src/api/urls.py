from django.conf.urls import url
from django.urls import path

from .views import AllQuestionsView, QuestionView, UserList, UserDetail

app_name = 'api'

urlpatterns = [
    path('', AllQuestionsView.as_view(), name='allquestions'),
    path('<int:pk>/', QuestionView.as_view(), name='question'),
    path('users/',UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

