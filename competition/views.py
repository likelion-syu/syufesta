from django.shortcuts import render
from .models import Booth
from . serializers import BoothSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse


class BoothViewSet(viewsets.ModelViewSet):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer

def event(req):
    return render (req, 'competition/event.html')

def foodtruck(req):
    if req.method == 'GET':
        foods = Booth.objects.all()
        serializer = BoothSerializer(foods, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = BoothSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.errors, status=400)
    print(foods)
    return render (req, 'competition/foodtruck.html', {'foods':foods})

def timeline(req):
    return render (req, 'competition/timeline.html')

def notice(req):
    return render (req, 'competition/notice.html')

def seatmap(req):
    return render (req, 'competition/seatmap.html')
