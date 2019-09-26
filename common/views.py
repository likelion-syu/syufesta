from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
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


def fest_talent(req):
	with connection.cursor() as cursor:
		cursor.execute("select cont_participant_nm as name ,count(1) as 'cnt' , total from (select * from ContestVote join (select count(1) total from ContestVote) as temp) as CV join ContestParticipant As CP on CV.cont_participant_id = CP.cont_participant_id group by CP.cont_participant_id order by 'cnt' desc;")
		rows = cursor.fetchall()

	expanded_rows = []
	expanded_rows = utils.query_expand(rows , cursor)

	return JsonResponse({
		'status' : 1,
		'data' : expanded_rows,
	}, safe=False)