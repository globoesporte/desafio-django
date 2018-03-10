from django import template
register = template.Library()
from django.db.models import Sum
from ..models import Options,Survey

@register.filter(name='percentage')
def percentage(pk,act_votes):
    total_votes=Options.objects.filter(survey__pk=pk).aggregate(Sum('votes'))['votes__sum']
    try:
        if total_votes > 0:
            return "{0:.0f}".format(((float(act_votes) / float(total_votes)) * 100))
        else:
            return 0
    except ValueError:
        return ''
