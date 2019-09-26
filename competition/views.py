from django.shortcuts import render
from common.models import Booth
from common.models import Foodtruck
from common.models import Matchschedule
from common import utils

from django.db import connection

from django.http import HttpResponse, JsonResponse


def home(req):
    print('Hello World')
    return render(req , 'competition/competition_main.html')

def event(req):
    return render (req, 'competition/event.html')

def foodtruck(req):
    foodtruck = Foodtruck.objects.all()
    return render (req, 'competition/foodtruck.html', {'foodtrucks':foodtruck})

def foodtruck_detail(req):
    return render (req, 'competition/foodtruck_detail.html')

def timeline(req):
    with connection.cursor() as cursor:
        cursor.execute("select * from MatchSchedule")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows, cursor)
    
    return render(req , 'competition/timeline.html' , {
        'data' : expanded_rows
    })

def notice(req):
    return render (req, 'competition/notice.html')

def seatmap(req):
    return render (req, 'competition/seatmap.html')
