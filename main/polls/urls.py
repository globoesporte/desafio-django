from . import views

from django.conf.urls import url, include

urlpatterns = [
	url(r'^$', views.polls_list, name='polls-list'),
	url(r'^polls/(?P<pk>\d+)/$', views.polls_detail, name='polls-detail'),
	url(r'^polls/vote/(?P<poll_pk>\d+)/(?P<option_pk>\d+)/$', views.polls_vote, name='polls-vote'),
]