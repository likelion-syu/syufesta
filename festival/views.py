from django.shortcuts import render
from django.db import connection, transaction
from common.models import Booth
from common import utils
from django.http import JsonResponse

def my_custom_sql(self):
	with connection.cursor() as cursor:
		cursor.execute("UPDATE bar SET FOO = 1 WHERE baz = %s", [self.baz])
		cursor.execute("SELECT foo FROM bar WHERE baz= %s", [self.baz])
		row = cursor.fetchone()
	return row

def foodtruck (req):
	return render(req, 'festival/foodtruck.html')

def booth (req):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM Account")
		rows = cursor.fetchall()
	
	expanded_rows = []

	for row in rows:
		expanded_row = { }
		for idx , desc in enumerate(cursor.description):
			expanded_row[desc[0]] = row[idx]
		expanded_rows.append(expanded_row)

	return JsonResponse({
		'status' : 1,
		'data' : expanded_rows,
	}, safe=False)

def stamp (req):
	return render(req, 'festival/stamp.html')

# 투표 결과 나타내는 함수
def talent (req):
	with connection.cursor() as cursor:
		cursor.execute("SELECT CP.name , count(CP.name) as CT FROM ContestParticipant as CP JOIN ContestVote as CV ON CP.cont_participant_id = CV.cont_participant_id group by CP.name")
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
