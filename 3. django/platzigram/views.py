"""platzigram views"""

# Django
from django.http import HttpResponse

# utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs')
    return HttpResponse('oh hi! current server time is {now}'.format(now=str(now)))


def hi(request):
    """Hi"""
    print(request)
    return HttpResponse('Hi!')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {} eres mejor de edad'.format(name)
    else:
        message = 'Hello {} Bienvenido a platzigram'.format(name)
    return HttpResponse(message)
