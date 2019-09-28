from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from django.core import serializers
from .models import Major
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
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FoodTruck WHERE truck_id = " + str(pk))
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : expanded_rows[0]
    })



def comp_seatmap(req , pk):
    major_detail = get_object_or_404(Major, pk=pk)

    return render(req , 'common/popup/competition/seatmap.html', {'major': major_detail})


def talent_result(request):
    with connection.cursor() as cursor:
        cursor.execute("select * , (result.count / temp.total) * 100 as rate from ( select RCP.cp_id , RCP.cont_participant_nm, CASE WHEN TCP.cnt IS NULL THEN 0 ELSE TCP.cnt END as count , RCP.cont_participant_img_url from ContestParticipant as RCP left join ( select CP.cp_id, cont_participant_nm as name , count(1) as 'cnt' from ContestVote as CV join ContestParticipant As CP on CV.cp_id = CP.cp_id group by CP.cp_id order by 'cnt' desc ) as TCP on RCP.cp_id = TCP.cp_id ) as result join ( select count(1) total from ContestVote) as temp;")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)
    
    result_list = {'result': 1, 'data': expanded_rows}
    return JsonResponse(result_list, json_dumps_params={'ensure_ascii': False})


