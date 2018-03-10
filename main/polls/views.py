from polls.models import (
	Poll,
	Option,
	Vote,
)

from django.shortcuts import (
	render,
	redirect,
	get_object_or_404,
)


def polls_list(request):
	template = 'polls_list.html' 
	context = {
		'polls': Poll.objects.all(),
		'page_title': 'Lista de Enquetes',
	}
	return render(request, template, context)


def polls_detail(request, pk):
	poll = get_object_or_404(Poll, pk=pk)
	template = 'polls_detail.html' 
	context = {
		'poll': poll,
		'page_title': poll.title,
	}
	return render(request, template, context)


def polls_vote(request, poll_pk, option_pk):
	template = 'polls_vote.html'

	poll = get_object_or_404(Poll, pk=poll_pk)
	option = get_object_or_404(Option, pk=option_pk)
	
	vote = Vote.objects.create(
		poll=poll,
		options=option,
	)

	context = {
		'vote': vote,
		'page_title': vote.poll.title,
	}

	return render(request, template, context)