from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

app_name = 'post'


def index(request):
    return HttpResponse('Главная страница')


def group_post(request, slug):
    return HttpResponse('Групповые посты')