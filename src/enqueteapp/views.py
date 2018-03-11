from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'enqueteapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'enqueteapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'enqueteapp/results.html'

def vote(request, question_id):
    # Tem que mudar essa merda pra não salvar direto, tem que fzr o lance de
    # guardar na memória e salvar dps de 1 minuto
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('enqueteapp:results', args=(question.id,)))
