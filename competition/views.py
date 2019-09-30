from django.shortcuts import render
from common.models import Booth, Foodtruck, Matchschedule, Major
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
        cursor.execute("select MS.* ,MJ_A.major_name as 'major_a_name' ,MJ_A.major_logo_url as 'major_a_logo_url' ,MJ_B.major_name as 'major_b_name' ,MJ_B.major_logo_url as 'major_b_logo_url'from MatchSchedule as MS join Major as MJ_A join Major as MJ_B on MS.sch_major_a = MJ_A.major_id and MS.sch_major_b = MJ_B.major_id")
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
    
def major_data(req):
    major_data = Major.objects.all()
    return render (req, 'competition/test.html', {'major':major_data})

def data_test(req):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ContestVote")
        rows = cursor.fetchall()

    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return JsonResponse({
        'server' : 1,
        'data' : expanded_rows,
    }, safe=False)