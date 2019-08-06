from django.shortcuts import render


def index(request):
    return render(request, 'surveys/surveys.html')

def survey(request):
   return render(request, 'surveys/survey.html')

def search(request):
   return render(request, 'surveys/search.html')