from django.shortcuts import render


# Create your views here.



def compete_event(request):
    return render (request, 'competition/compete_event.html')

def food_truck(request):
    return render (request, 'competition/compete_food_truck.html')

def compete_timeline(request):
    return render (request, 'competition/compete_timeline.html')

def safety(request):
    return render (request, 'competition/safety.html')

def seat_map(request):
    return render (request, 'competition/seat_map.html')
