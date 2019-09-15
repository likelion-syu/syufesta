from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Major, Student

# Create your views here.

def com_home(request):
    return render (request, 'competition/index.html')

def com_event(request):
    return render (request, 'competition/compete_event.html')

def com_ft(request):
    return render (request, 'competition/compete_food_truck.html')

def com_tl(request):
    majors = Major.objects.all()
    return render (request, 'competition/compete_timeline.html', {'majors':majors})

def com_tl_detail(request, major_id):
    major_detail = get_object_or_404(Major, pk = major_id)
    student = Student.objects.all()
    return render(request, 'competition/com_tl_detail.html', {'player':major_detail, 'students':student})

def com_safety(request):
    return render (request, 'competition/safety.html')

def com_sm(request):
    return render (request, 'competition/seat_map.html')
