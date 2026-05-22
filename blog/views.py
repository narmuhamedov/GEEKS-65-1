from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World')

def persons_mk_view(request):
    if request.method == "GET":
        context = {
            'title': 'Scorpion',
            'name': 'Hanzo Hasashi',
            'time': datetime.now(),
            'capabilities':[
                'kunai',
                'katana',
                'fire',
                'fatality fire'
            ]
        }
    return render(request, 'persons_mk.html', context)