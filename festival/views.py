from django.shortcuts import render , redirect
from django.db import connection, transaction
from common.models import Booth, Boothstamp, Contestparticipant, AuthUser, Contestvote
from common import utils
from django.http import JsonResponse

def main(req):
	return render(req, 'festival/festival_main.html')

def my_custom_sql(self):
	with connection.cursor() as cursor:
		cursor.execute("UPDATE bar SET FOO = 1 WHERE baz = %s", [self.baz])
		cursor.execute("SELECT foo FROM bar WHERE baz= %s", [self.baz])
		row = cursor.fetchone()
	return row

def foodtruck (req):
	return render(req, 'festival/foodtruck.html')

def festmap (req):
	return render(req, 'festival/festmap.html')

def stamp (req):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * from BoothStamp")
	expanded_rows = []
	expanded_rows = utils.query_expand(rows , cursor)

	return render(req, 'festival/stamp.html',{
		'data' : expanded_rows
	})

def stamp_data (req):
    with connection.cursor() as cursor:
        cursor.execute("select * from BoothStamp;")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)
    
    result_list = {'result': 1, 'data': expanded_rows}
    return JsonResponse(result_list, json_dumps_params={'ensure_ascii': False})


def stamp_visit(req):
	return render(req , 'festival/stamp.visit.html')


# 투표
def talent_select(req):
	if req.user.is_authenticated :
		cur_vote = Contestvote.objects.filter(cv_account_id=req.user.id)
		if cur_vote :
			return redirect('talent')

	cp_vote = Contestvote.objects.all()
	contestparticipant=Contestparticipant.objects.all().order_by('cont_participant_order')
	
	return render(req, 'festival/talent.html', {'cp':contestparticipant}, {'cp_vote':cp_vote})

# 투표 결과 나타내는 함수
def talent (req):
	with connection.cursor() as cursor:
		cursor.execute("select count(1) as 'cnt' , cont_participant_nm as name , total from (select * , ROW_COUNT() as total from ContestVote) as CV join ContestParticipant As CP on CV.cp_id = CV.cp_id group by CV.cp_id order by 'cnt' desc;")
		rows = cursor.fetchall()

	expanded_rows = []
	expanded_rows = utils.query_expand(rows , cursor)

	return render(req, 'festival/talent_contest.html',{
		'data' : expanded_rows
	})

def cheer(req):
	return render(req, 'festival/cheer_contest.html')

def popup1(req):
	return render(req, 'festival/foodtruck1.html')

def signin(req) :
	return render(req , 'festival/auth/signin.html')

def signup(req) :
	return render(req , 'festival/auth/signup.html')

def signout(req) : 
	print("signout")

