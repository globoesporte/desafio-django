from django import template

register = template.Library()


@register.simple_tag
def percentual(valor, total):
    if total == 0:
        return 0
    return valor/total * 100
