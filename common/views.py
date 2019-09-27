from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from . import utils
# Create your views here.
def home(request):
    return render (request, 'common/index.html')

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
		cursor.execute("SELECT CP.name , count(CP.name) FROM ContestParticipant as CP JOIN ContestVote as CV ON CP.cont_participant_id = CV.cont_participant_id group by CP.name")
		rows = cursor.fetchall()

	expanded_rows = []
	expanded_rows = utils.query_expand(rows , cursor)

	return JsonResponse({
		'status' : 1,
		'data' : expanded_rows,
<<<<<<< HEAD
	}, safe=False)
=======
	}, safe=False)
>>>>>>> 8a1b57b69fb100e564da94b198f2301fbda91f7a
