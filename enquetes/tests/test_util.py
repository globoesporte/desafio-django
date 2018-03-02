from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from rest_framework.test import APIClient

from requests.auth import HTTPBasicAuth


# Utilitários de comparação de estruturas de listas de dicionários
def isDict(o):
    return type(o) is dict or o.__class__.__name__ == 'OrderedDict'


def isList(o):
    return type(o) is list or o.__class__.__name__ == 'ReturnList'


def equalDicts(d1, d2):
    for k in d1.keys():
        if k not in d2:
            return False
        else:
            if isDict(d1[k]):
                if not equalDicts(d1[k], d2[k]):
                    return False
            elif isList(d1[k]):
                return equalListDicts(d1[k], d2[k])
            elif d1[k] != d2[k]:
                return False

    return True


def equalListDicts(l1, l2):

    found = False

    if(isList(l1) and isList(l2)):
        for i1 in l1:
            for i2 in l2:
                if isDict(i1) and isDict(i2):
                    if equalDicts(i1, i2):
                        found = True
                        break
            if found:
                break
    return found
