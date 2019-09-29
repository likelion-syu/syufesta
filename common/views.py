from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from .models import Major, Foodtruck, FoodtruckMenu, Booth, Contestparticipant
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

def fest_foodtruck(req, pk):
    foodtruck_detail = get_object_or_404 (Foodtruck, pk=pk)
    foodtruck_menu = FoodtruckMenu.objects.filter(truck = pk)
    return render(req, 'common/popup/festival/foodtruck.html', {'food': foodtruck_detail, 'menus':foodtruck_menu})

def fest_booth(req, pk):
    booth_detail = get_object_or_404(Booth, pk=pk)
    return render(req, 'common/popup/festival/booth.html', {'booth': booth_detail})

def talent_result(request):
    with connection.cursor() as cursor:
        cursor.execute("select * , (result.count / temp.total) * 100 as rate from ( select RCP.cp_id , RCP.cont_participant_nm, CASE WHEN TCP.cnt IS NULL THEN 0 ELSE TCP.cnt END as count , RCP.cont_participant_img_url from ContestParticipant as RCP left join ( select CP.cp_id, cont_participant_nm as name , count(1) as 'cnt' from ContestVote as CV join ContestParticipant As CP on CV.cp_id = CP.cp_id group by CP.cp_id order by 'cnt' desc ) as TCP on RCP.cp_id = TCP.cp_id ) as result join ( select count(1) total from ContestVote) as temp;")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)
    
    result_list = {'result': 1, 'data': expanded_rows}
    return JsonResponse(result_list, json_dumps_params={'ensure_ascii': False})


	# return JsonResponse({
	# 	'status' : 1,
	# 	'data' : expanded_rows,
	# }, safe=False)
