from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_survey', views.survey, name='create_survey'),
]
