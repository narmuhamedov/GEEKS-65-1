from django.shortcuts import render
from . import models


def car_list_view(request):
    if request.method == 'GET':
        auto = models.Car.objects.all()
        context = {
            'cars': auto,
        }
    return render(request, template_name='cars.html', context=context)

