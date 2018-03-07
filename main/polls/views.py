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
		'polls': Poll.objects.all()
	}
	return render(request, template, context)


def polls_detail(request, pk):
	template = 'polls_detail.html' 
	context = {
		'poll': get_object_or_404(Poll, pk=pk)
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
	}

	return render(request, template, context)