from django.shortcuts import render

def foodtruck (req):
	return render(req, 'festival/foodtruck.html')

def booth (req):
	return render(req, 'festival/booth.html')

def stamp (req):
	return render(req, 'festival/stamp.html')

def talent (req):
	return render(req, 'festival/talent_contest.html')

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