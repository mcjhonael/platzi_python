
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def list_posts(request):
    posts = [1, 4, 5, 6]
    return HttpResponse(str(posts))

