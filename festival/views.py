from django.shortcuts import render
from django.db import connection
from competition.models import Booth

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

def talent (req):
	return render(req, 'festival/talent_contest.html')

def cheer(req):
	return render(req, 'festival/cheer_contest.html')

def popup1(req):
	return render(req, 'festival/foodtruck1.html')
	