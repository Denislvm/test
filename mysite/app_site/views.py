from django.shortcuts import render
from django.http import HttpResponse


def test_app(request):
    return HttpResponse('Hello world')