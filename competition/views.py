from django.shortcuts import render
from .models import Booth


from django.http import HttpResponse, JsonResponse


def event(req):
    return render (req, 'competition/event.html')

def foodtruck(req):
    return render (req, 'competition/foodtruck.html')

def timeline(req):
    return render (req, 'competition/timeline.html')

def notice(req):
    return render (req, 'competition/notice.html')

def seatmap(req):
    return render (req, 'competition/seatmap.html')
