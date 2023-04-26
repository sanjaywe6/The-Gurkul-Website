from logging import exception
from django.shortcuts import redirect, render
from gurkul_admin.models import *
from gurkul_teacher.models import *
from gurkul_test.models import *
from django.contrib import messages
from django.http import JsonResponse
from thegurkul.the_gurkul_functions import *
from . import gurkul_test_functions

# Create your views here.

def GTA_index(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)
    if user_type=='teacher':
            teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
            auth_to_add_series=teacher_auth.objects.filter(teacher_id=teacher_id).first().edit_test_series
            if auth_to_add_series==True:
                generated_form_options=gurkul_test_functions.get_form_optioins()
                param={'generated_form_options':generated_form_options}
                return render(request,'gurkul_test/add_gta_question.html',param)
            else:
                return redirect('/')
    else:
        return redirect('/')

def get__GTA_question_form(request):
    if request.method=='POST':
        # input data fields to know whether question is new or old
        form_status = request.POST.get('form_status')
        qid = request.POST.get('qid')
        # variable values to send next question id to server
        get_empty_question_id=request.POST.get('get_empty_question_id')
        if get_empty_question_id=='True':
            last_id=gta_all_question.objects.last().sno
            next_id=f"GTA0{last_id+1}"
            return JsonResponse({'next_id':next_id})
        # input data of questions
        input_category=request.POST.get('input_category')
        input_language=request.POST.get('input_language')
        input_board=request.POST.get('input_board')
        input_standard=request.POST.get('input_standard')
        input_subject=request.POST.get('input_subject')
        input_qtype=request.POST.get('input_qtype')

        input_question=request.POST.get('input_question')

        # question options 
        radio_option=request.POST.get('radio_option')

        input_option_1=request.POST.get('input_option_1')

        input_option_2=request.POST.get('input_option_2')

        input_option_3=request.POST.get('input_option_3')

        input_option_4=request.POST.get('input_option_4')

        input_answer=request.POST.get('input_answer')


        submit_form=gurkul_test_functions.submit_gta_form(request,input_category,input_language,input_board,input_standard,input_subject,input_qtype,input_question,radio_option,input_option_1,input_option_2,input_option_3,input_option_4,input_answer,form_status,qid)
            
        return JsonResponse({'status':submit_form,'input_category':input_category,'input_language':input_language,'input_board':input_board,'input_standard':input_standard,'input_subject':input_subject,'input_qtype':input_qtype})

    else:
        return JsonResponse({'code':400})


def return_gta_question(request):
    if request.method=='POST':
        input_category=request.POST.get('input_category')
        input_language=request.POST.get('input_language')
        input_board=request.POST.get('input_board')
        input_standard=request.POST.get('input_standard')
        input_subject=request.POST.get('input_subject')
        input_qtype=request.POST.get('input_qtype')

        get_question=gta_all_question.objects.filter(question_category=input_category,language=input_language,board=input_board,standard=input_standard,subject=input_subject,qtype=input_qtype).values()

        questions_len=len(get_question)

        lst=[]

        for item in get_question:
            lst.append(item)
        lst.reverse()

        return JsonResponse({'code':200,'all_question':lst,'question_category':input_category,'language':input_language,'board':input_board,'standard':input_standard,'subject':input_subject,'qtype':input_qtype,'questions_len':questions_len})
    
    else:
        return JsonResponse({'code':400})


def return_question_with_id(request):
    if request.method == 'POST':
        qid=request.POST.get('qid')
        question=gta_all_question.objects.filter(id=qid).values()
        question=list(question)
        return JsonResponse({'code':200,'question':question})
    
    else:
        return JsonResponse({'code':400})