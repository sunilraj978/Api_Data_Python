from django.shortcuts import render
import speech_recognition as sr

import requests

# Create your views here.
from .models import Poll


def ok(request):
    return render(request, 'ok.htm')


def home(request):
    # response = requests.get('https://breakingbadapi.com/api/characters').json()
    # for i in response:
    #     data = Poll(image=i['img'], occupation=i['occupation'][0], status=i['status'], nickname=i['name'],
    #                 portrayed=i['portrayed'])
    #     data.save()
    name = request.GET.get('title_contains')
    if name is None:
        response = Poll.objects.all()
    else:
        response = Poll.objects.order_by(name)

    return render(request, 'home.html', {'response': response})


def filterData(request):
    response = requests.get('https://breakingbadapi.com/api/characters').json()
    name = request.GET.get('title_contains')

    if name != '' and name is not None:
        list1 = []
        for i in response:
            name1 = i['name'].split()
            if name in name1:
                response = i
                list1.append(response)
                print(list1)

    if name is None:
        context = {
            'queryset': response,
        }
        return render(request, 'Form.html', context)
    else:
        context = {
            'queryset': list1
        }
        return render(request, 'Form2.html', context)
