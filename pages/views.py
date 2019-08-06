from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def survey(request):
    return render(request, 'pages/create_survey.html')
