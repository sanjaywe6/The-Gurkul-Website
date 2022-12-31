from logging import exception
from django.shortcuts import redirect, render
from gurkul_admin.models import *
from gurkul_teacher.models import *
from gurkul_test.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

# function to forwarding user to add/edit test series
def gurkul_test_index(request):
    if str(request.user)=='AnonymousUser':
        return render(request,'gurkul_test/all_test_series.html')
    else:
        user=all_usrs.objects.filter(userProfile=request.user)
        usertype=user[0].visitor_type 
        if usertype=='student':
                return render(request,'gurkul_test/all_test_series.html')
        elif usertype=='teacher':
            teacher_id=user[0].teacher_id
            teacher_per=teacher_auth.objects.filter(teacher_id=teacher_id).first()
            permi=teacher_per.edit_test_series
       
            if permi==True:
                return render(request,'gurkul_test/add_test_series.html')
            else:
                return render(request,'gurkul_test/all_test_series.html')
        else:
            return render(request,'gurkul_test/all_test_series.html')

# funtion to get post data of adding academic test series categories
def academic_test_series_category(request):
    if request.method=='POST':
        language=request.POST.get('language')
        test_class=request.POST.get('class')
        test_board=request.POST.get('board')
        test_qtype=request.POST.get('qtype')
        test_subject=request.POST.get('subject')
        test_question=request.POST.get('question')
        test_acad_q_1=request.POST.get('acad_q_1')
        test_acad_q_2=request.POST.get('acad_q_2')
        test_acad_q_3=request.POST.get('acad_q_3')
        test_acad_q_4=request.POST.get('acad_q_4')
        test_answer=request.POST.get('answer')
        type=request.POST.get('type')
        q_id=request.POST.get('acad_q_id')
        if int(q_id)<0:
            if type=='show_questions':
                questions=gurkul_academic_test_series_model.objects.filter(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype).values().reverse()
                questions=list(questions)

                length=len(questions)
                return JsonResponse({'status':'200','msg':'Your MCQ Question has been added to Model...','questions':questions,'class':test_class,'board':test_board,'subject':test_subject,'qtype':test_qtype,'length':length})
            else:
                if len(test_question)>=0:
                    if test_qtype=="MCQ":
                        if len(test_acad_q_1)>0:
                            if len(test_acad_q_2)>0:
                                if len(test_acad_q_3)>0:
                                    if len(test_acad_q_4)>0:
                                        # matching question with existing database
                                        question_from_db=gurkul_academic_test_series_model.objects.filter(question=test_question,acad_q_1=test_acad_q_1,acad_q_2=test_acad_q_2,acad_q_3=test_acad_q_3,acad_q_4=test_acad_q_4)
                                        if len(question_from_db)<1:
                                            add_question=gurkul_academic_test_series_model(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype,question=test_question,acad_q_1=test_acad_q_1,acad_q_2=test_acad_q_2,acad_q_3=test_acad_q_3,acad_q_4=test_acad_q_4,answer=test_answer,user_profile=request.user)
                                            add_question.save()
                                            questions=gurkul_academic_test_series_model.objects.filter(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype).values()
                                            questions=list(questions)
                                            length=len(questions)
                                            return JsonResponse({'status':'200','msg':'Your MCQ Question has been added to Model...','questions':questions,'class':test_class,'board':test_board,'subject':test_subject,'qtype':test_qtype,'length':length})
                                        else:
                                            return JsonResponse({'status':'400','msg':'Sorry! This question already exist in database...'})
                                    else:
                                        return JsonResponse({'status':'400','msg':'Sorry! Fourth Option was empty...'})
                                else:
                                    return JsonResponse({'status':'400','msg':'Sorry! Third Option was empty...'})

                            else:
                                return JsonResponse({'status':'400','msg':'Sorry! Second Option was empty...'})
                        else:
                            return JsonResponse({'status':'400','msg':'Sorry! First Option was empty...'})             
                    elif (test_qtype=="Short" or test_qtype=="Long" or test_qtype=="Very Long"):
                        add_question=gurkul_academic_test_series_model(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype,question=test_question,user_profile=request.user)
                        add_question.save()
                        questions=gurkul_academic_test_series_model.objects.filter(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype).values()
                        questions=list(questions)
                        length=len(questions)
                        return JsonResponse({'status':'200','msg':'Your Question has been added to Model...','questions':questions,'class':test_class,'board':test_board,'subject':test_subject,'qtype':test_qtype,'length':length})
                    else:
                        return JsonResponse({'status':'400','msg':'Question type is not define'})
                else:
                    return JsonResponse({'status':'400'}) 
        else:
            if type=='show_questions':
                questions=gurkul_academic_test_series_model.objects.filter(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype).values().reverse()
                questions=list(questions)

                length=len(questions)
                return JsonResponse({'status':'200','msg':'Your MCQ Question has been added to Model...','questions':questions,'class':test_class,'board':test_board,'subject':test_subject,'qtype':test_qtype,'length':length})
            else:
                if len(test_question)>0:
                    if test_qtype=="MCQ":
                        if len(test_acad_q_1)>0:
                            if len(test_acad_q_2)>0:
                                if len(test_acad_q_3)>0:
                                    if len(test_acad_q_4)>0:
                                        add_question=gurkul_academic_test_series_model(sno=q_id,language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype,question=test_question,acad_q_1=test_acad_q_1,acad_q_2=test_acad_q_2,acad_q_3=test_acad_q_3,acad_q_4=test_acad_q_4,answer=test_answer,user_profile=request.user)
                                        add_question.save()
                                        questions=gurkul_academic_test_series_model.objects.filter(language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype).values()
                                        questions=list(questions)
                                        length=len(questions)
                                        return JsonResponse({'status':'200','msg':'Your MCQ Question has been updated in the Model...','questions':questions,'class':test_class,'board':test_board,'subject':test_subject,'qtype':test_qtype,'length':length})

                                    else:
                                        return JsonResponse({'status':'400','msg':'Sorry! Fourth Option was empty...'})
                                else:
                                    return JsonResponse({'status':'400','msg':'Sorry! Third Option was empty...'})

                            else:
                                return JsonResponse({'status':'400','msg':'Sorry! Second Option was empty...'})
                        else:
                            return JsonResponse({'status':'400','msg':'Sorry! First Option was empty...'})             
                    elif (test_qtype=="Short" or test_qtype=="Long" or test_qtype=="Very Long"):
                        add_question=gurkul_academic_test_series_model(sno=q_id,language=language,test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype,question=test_question,user_profile=request.user)
                        add_question.save()
                        questions=gurkul_academic_test_series_model.objects.filter(test_class=test_class,board=test_board,subject=test_subject,qtype=test_qtype).values()
                        questions=list(questions)
                        length=len(questions)
                        return JsonResponse({'status':'200','msg':'Your Question has been updated in the Model...','questions':questions,'class':test_class,'board':test_board,'subject':test_subject,'qtype':test_qtype,'length':length})
                    else:
                        return JsonResponse({'status':'400','msg':'Sorry! Question type is not define'})
                else:
                    return JsonResponse({'status':'400'}) 
            

# funtion to get post data of adding competition test series categories
def competition_test_series_category(request):
    if request.method=='POST':
        exam_type=request.POST.get('exam_type')
        subject=request.POST.get('subject')
        qtype=request.POST.get('qtype')
        question=request.POST.get('question')
        comp_q_1=request.POST.get('comp_q_1')
        comp_q_2=request.POST.get('comp_q_2')
        comp_q_3=request.POST.get('comp_q_3')
        comp_q_4=request.POST.get('comp_q_4')
        answer=request.POST.get('answer')
        type=request.POST.get('type')
        q_id=request.POST.get('q_id')
        language=request.POST.get('language')

        if int(q_id)<0:
            if type=='show_questions':
                questions=gurkul_competition_test_series_model.objects.filter(language=language,exam_type=exam_type,subject=subject,qtype=qtype).values().reverse()
                questions=list(questions)
                length=len(questions)
                return JsonResponse({'status':'200','msg':'Your MCQ Question has been added to Model...','questions':questions,'exam_type':exam_type,'subject':subject,'qtype':qtype,'length':length})

            else:
                if len(question)>0:

                    if len(comp_q_1)>0:
                        if len(comp_q_2)>0:
                            if len(comp_q_3)>0:
                                if len(comp_q_4)>0:
                                    # matching question with existing database
                                    question_from_db=gurkul_competition_test_series_model.objects.filter(question=question,option_1=comp_q_1,option_2=comp_q_2,option_3=comp_q_3,option_4=comp_q_4)
                                    if len(question_from_db)<1:
                                        add_question=gurkul_competition_test_series_model(language=language,exam_type=exam_type,subject=subject,qtype=qtype,question=question,option_1=comp_q_1,option_2=comp_q_2,option_3=comp_q_3,option_4=comp_q_4,answer=answer,user_profile=request.user)
                                        add_question.save()
                                        questions=gurkul_competition_test_series_model.objects.filter(exam_type=exam_type,subject=subject,qtype=qtype).values()
                                        questions=list(questions)
                                        length=len(questions)
                                        return JsonResponse({'status':'200','msg':'Your MCQ Question has been added to Model...','questions':questions,'exam_type':exam_type,'subject':subject,'qtype':qtype,'length':length})
                                    else:
                                        return JsonResponse({'status':400,'msg':'Sorry! This question already exist in database..'})
                                else:
                                    return JsonResponse({'status':400,'msg':'Sorry! Fourth option was empty....'})
                            else:
                                return JsonResponse({'status':400,'msg':'Sorry! Third option was empty....'})
                        else:
                            return JsonResponse({'status':400,'msg':'Sorry! Second option was empty....'})
                    else:
                        return JsonResponse({'status':400,'msg':'Sorry! First option was empty....'})
                else:
                    return JsonResponse({'status':400,'msg':'Sorry! Question field can not empty....'})
        else:
            if type=='show_questions':
                questions=gurkul_competition_test_series_model.objects.filter(language=language,exam_type=exam_type,subject=subject,qtype=qtype).values().reverse()
                questions=list(questions)
                length=len(questions)
                return JsonResponse({'status':'200','msg':'Your MCQ Question has been added to Model...','questions':questions,'exam_type':exam_type,'subject':subject,'qtype':qtype,'length':length})

            else:
                if len(question)>0:
                 
                    if len(comp_q_1)>0:
                        if len(comp_q_2)>0:
                            if len(comp_q_3)>0:
                                if len(comp_q_4)>0:
                                    add_question=gurkul_competition_test_series_model(sno=q_id,language=language,exam_type=exam_type,subject=subject,qtype=qtype,question=question,option_1=comp_q_1,option_2=comp_q_2,option_3=comp_q_3,option_4=comp_q_4,answer=answer,user_profile=request.user)
                                    add_question.save()
                                    questions=gurkul_competition_test_series_model.objects.filter(exam_type=exam_type,subject=subject,qtype=qtype).values()
                                    questions=list(questions)
                                    length=len(questions)
                                    return JsonResponse({'status':'200','msg':'Your MCQ Question has been updated in Model...','questions':questions,'exam_type':exam_type,'subject':subject,'qtype':qtype,'length':length})
                                else:
                                    return JsonResponse({'status':400,'msg':'Sorry! Fourth option was empty....'})
                            else:
                                return JsonResponse({'status':400,'msg':'Sorry! Third option was empty....'})
                        else:
                            return JsonResponse({'status':400,'msg':'Sorry! Second option was empty....'})
                    else:
                        return JsonResponse({'status':400,'msg':'Sorry! First option was empty....'})
                else:
                    return JsonResponse({'status':400,'msg':'Sorry! Question field can not empty....'})


#  function for sending filterder question to database for editing edtitng test series question
def edit_test_series(request):
    if request.method=='POST':
        q_sno=request.POST.get('id')
        class_type=request.POST.get('class_type')
    
        if class_type=='acad':
            question=gurkul_academic_test_series_model.objects.filter(sno=q_sno).first()
            q_type=question.qtype
            if q_type=='MCQ':
                question=gurkul_academic_test_series_model.objects.filter(sno=q_sno).values()
                question=list(question)
                return JsonResponse({'status':200,'question':question,'class':class_type,'qtype':'MCQ'})
            else:
                question=gurkul_academic_test_series_model.objects.filter(sno=q_sno).values()
                question=list(question)
                return JsonResponse({'status':200,'question':question,'class':class_type,'qtype':'other'})
        elif class_type=='comp':
            question=gurkul_competition_test_series_model.objects.filter(sno=q_sno).first()
            q_type=question.qtype
            if q_type=='MCQ':
                question=gurkul_competition_test_series_model.objects.filter(sno=q_sno).values()
                question=list(question)
                return JsonResponse({'status':200,'question':question,'class':class_type,'qtype':'MCQ'})
            else:
                question=gurkul_competition_test_series_model.objects.filter(sno=q_sno).values()
                question=list(question)
                return JsonResponse({'status':200,'question':question,'class':class_type,'qtype':'other'})

    return JsonResponse({'status':200})