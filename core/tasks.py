from background_task import background
from django.contrib.auth.models import User
from .models import Options

@background(schedule=60)
def vote(survey_,pk_,number):
    option = Options.objects.filter(survey__pk=survey_).get(pk=pk_)
    option.vote(pk_, number)
