from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from .models import Major, Foodtruck, FoodtruckMenu
from . import utils


# from models import Booth , FoodTruck
# Create your views here.
def home(request):
    return render (request, 'common/index.html')

def comp_booth(req , pk):
    with connection.cursor() as cursor:
        cursor.execute("select * from Booth where booth_id = " + str(pk))
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows, cursor)
    
    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : expanded_rows[0]
    })

def comp_foodtruck(req , pk):
    foodtruck_detail = get_object_or_404(Foodtruck, pk=pk)
    foodtruck_menu = FoodtruckMenu.objects.filter(truck = pk)

    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : foodtruck_detail, 'menus': foodtruck_menu
    })



def comp_seatmap(req , pk):
    major = get_object_or_404(Major, pk=pk)

    with connection.cursor() as cursor:
        cursor.execute("select TEMP.* , MJ_A.major_name as 'major_a_name' , MJ_A.major_logo_url as 'major_a_logo'  , MJ_B.major_name as 'major_b_name' , MJ_B.major_logo_url as 'major_b_logo' from ( select * from MatchSchedule where sch_major_a = "+str(pk)+" or sch_major_b = "+str(pk)+" ) TEMP JOIN Major as MJ_A JOIN Major as MJ_B on TEMP.sch_major_a = MJ_A.major_id and TEMP.sch_major_b = MJ_B.major_id")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return render(req , 'common/popup/competition/seatmap.html' , {
        'data' : expanded_rows , 'majors' : major 
    })

    # major_detail = get_object_or_404(Major, pk=pk)

    # return render(req , 'common/popup/competition/seatmap.html', {'major': major_detail})


	# return JsonResponse({
	# 	'status' : 1,
	# 	'data' : expanded_rows,
	# }, safe=False)
