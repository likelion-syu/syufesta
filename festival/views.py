from django.shortcuts import render
from django.db import connection, transaction
from common.models import Booth, Boothstamp
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
	return render(req, 'festival/stamp.html')

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

def talent_select(req):
	contestparticipant=Contestparticipant.objects.all()
	return render(req, 'festival/talent.html', {'cp':contestparticipant})

def signin(req) :
	return render(req , 'festival/auth/signin.html')

def signup(req) :
	return render(req , 'festival/auth/signup.html')

def signout(req) : 
	print("signout")
