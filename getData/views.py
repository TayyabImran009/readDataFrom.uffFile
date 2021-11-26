from django.http.response import HttpResponse
from django.shortcuts import render
from .models import info

# Create your views here.


def getData(request):
    print("Here")
    events = info(data="data1")
    events.save()
    return HttpResponse("Hello Data is saved")
