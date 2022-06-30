from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Сначала не было ничего')


def group_posts(request, slug):
    return HttpResponse(f'Тут кто-то что-то написал про {slug}')
