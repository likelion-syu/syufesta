from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from .models import Major, Foodtruck, FoodtruckMenu, Booth, Contestparticipant , Contestvote ,AuthUser
from . import utils
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


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
    foodtruck_detail = get_object_or_404(Foodtruck, pk=pk)
    foodtruck_menu = FoodtruckMenu.objects.filter(truck = pk)

    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : foodtruck_detail, 'menus': foodtruck_menu
    })



def comp_seatmap(req , pk):
    major = get_object_or_404(Major, pk=pk)

    with connection.cursor() as cursor:
        cursor.execute("select TEMP.* , MJ_A.major_name as 'major_a_name' , MJ_A.major_logo_url as 'major_a_logo'  , MJ_B.major_name as 'major_b_name' , MJ_B.major_logo_url as 'major_b_logo' from ( select * from MatchSchedule where sch_major_a = "+str(pk)+" or sch_major_b = "+str(pk)+" ) TEMP JOIN Major as MJ_A JOIN Major as MJ_B on TEMP.sch_major_a = MJ_A.major_id and TEMP.sch_major_b = MJ_B.major_id")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return render(req , 'common/popup/competition/seatmap.html' , {
        'data' : expanded_rows , 'majors' : major 
    })

    # major_detail = get_object_or_404(Major, pk=pk)

    # return render(req , 'common/popup/competition/seatmap.html', {'major': major_detail})

def fest_foodtruck(req, pk):
    foodtruck_detail = get_object_or_404 (Foodtruck, pk=pk)
    foodtruck_menu = FoodtruckMenu.objects.filter(truck = pk)
    return render(req, 'common/popup/festival/foodtruck.html', {'food': foodtruck_detail, 'menus':foodtruck_menu})

def fest_booth(req, pk):
    booth_detail = get_object_or_404(Booth, pk=pk)
    return render(req, 'common/popup/festival/booth.html', {'booth': booth_detail})

def talent_result(request):
    with connection.cursor() as cursor:
        cursor.execute("select * , (result.count / temp.total) * 100 as rate from ( select RCP.cp_id , RCP.cont_participant_nm, CASE WHEN TCP.cnt IS NULL THEN 0 ELSE TCP.cnt END as count , RCP.cont_participant_img_url from ContestParticipant as RCP left join ( select CP.cp_id, cont_participant_nm as name , count(1) as 'cnt' from ContestVote as CV join ContestParticipant As CP on CV.cp_id = CP.cp_id group by CP.cp_id order by 'cnt' desc ) as TCP on RCP.cp_id = TCP.cp_id ) as result join ( select count(1) total from ContestVote) as temp order by result.count desc , result.cont_participant_nm asc;")
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    result_list = {'result': 1, 'data': expanded_rows}
    return JsonResponse(result_list, json_dumps_params={'ensure_ascii': False})

def  festmap_popup1(req):
    return render(req, 'common/popup/festival/festmap_popup1.html')

def  festmap_popup2(req):
    return render(req, 'common/popup/festival/festmap_popup2.html')

def  festmap_popup3(req):
    return render(req, 'common/popup/festival/festmap_popup3.html')


# ============= API
@csrf_exempt
def contest_vote(req):    
    # 회원 가입 확인
    if not req.user.is_authenticated:
        return JsonResponse({
            'status' : -1,
            'err_desc' : '로그인 되지 않은 사용자압니다',
            'err_display_mesg' : '로그인이 필요합니다!\n메뉴의 간편 로그인을 이용해주세요!'
        } , json_dumps_params={ 'ensure_ascii' : False })
    # 정보 확인
    if 'cp_id' not in req.POST:
        return JsonResponse({
            'status' : -2,
            'err_desc' : '키가 존재하지 않음',
            'err_display_mesg' : '일시적인 오류가 발생했습니다 잠시 후 다시 시도해주세요'
        } , json_dumps_params={ 'ensure_ascii' : False })
    if not req.POST.get('cp_id') or req.POST.get('cp_id') == '':
        return JsonResponse({
            'status' : -3,
            'err_desc' : '키가 공백임',
            'err_display_mesg' : '일시적인 오류가 발생했습니다 잠시 후 다시 시도해주세요'
        } , json_dumps_params={ 'ensure_ascii' : False })
    
    cur_user_id = req.user.id
    cur_cp_id = req.POST.get('cp_id')
    cur_vote_info = Contestvote.objects.filter(cv_account = cur_user_id)
    
    # 기존 투표 확인
    if cur_vote_info :
        return JsonResponse({
            'status' : -4,
            'err_desc' : '이미 투표한 회원',
            'err_display_mesg' : '이미 투표하셨습니다! 참여해주셔서 감사합니다!'
        } , json_dumps_params={ 'ensure_ascii' : False })
    
    new_vote = Contestvote(cv_account_id=cur_user_id , cp_id=cur_cp_id , create_dt=datetime.now())
    new_vote.save()
    
    return JsonResponse({
        'status' : 1,
        'mesg' : '투표하였습니다! 감사합니다!'
    } , json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def contest_revote(req):    
    if not req.user.is_authenticated:
        return JsonResponse({
            'status' : -1,
            'err_desc' : '로그인 되지 않은 사용자압니다',
            'err_display_mesg' : '로그인이 필요합니다!\n메뉴의 간편 로그인을 이용해주세요!'
        } , json_dumps_params={ 'ensure_ascii' : False })

    cur_user_id = req.user.id
    cur_vote_info = Contestvote.objects.filter(cv_account = cur_user_id)
    if cur_vote_info :
        cur_vote_info.delete()
    
    return JsonResponse({
        'status' : 1,
        'mesg' : '재투표하자!'
    } , json_dumps_params={'ensure_ascii': False})


def stamp_info(req , pk):
    # booth = Booth.objects.filter(booth_id = pk)
    # print(booth)
    with connection.cursor() as cursor:
        cursor.execute("select * from Booth where booth_id = " + str(pk))
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return JsonResponse({
        'status' : 1,
        'data' : expanded_rows[0]
    } , json_dumps_params={'ensure_ascii' : False })
