from gurkul_test.models import *
import json

def get_form_optioins():
    options={}
    # getting question id
    id=gta_all_question.objects.last().sno
    options['id']=f"GTA0{id+1}"
    # getting cotegory
    category=gta_all_question.question_category_choices
    options['category']=category
    # getting language
    languages=gta_all_question.language_choices
    options['language']=languages
    # getting board
    boards=gta_all_question.board_choices
    options['board']=boards
    # getting standard
    standards=gta_all_question.standard_choices
    options['standard']=standards
    # getting subjects
    subjects=gta_all_question.subject_choices
    options['subject']=subjects
    # getting question types
    qtypes=gta_all_question.qtype_choices
    options['qtype']=qtypes
    # getting answer choices
    answer_options=gta_all_question.answer_option_choices
    options['answer_option']=answer_options
    return options


def validate_gta_questions(input_category,input_language,input_board,input_standard,input_subject,input_qtype,input_question,radio_option,input_option_1,input_option_2,input_option_3,input_option_4,input_answer):

    lst=[]

    if len(input_category)>0:
        if len(input_language)>0:
            if len(input_board)>0:
                if len(input_standard)>0:
                    if len(input_subject)>0:
                        if len(input_qtype)>0:
                            if len(input_question)>0:
                                if len(input_answer)>0:
                                    if input_qtype == 'MCQ':
                                        if len(input_option_1)>0:
                                            if len(input_option_2)>0:
                                                if len(input_option_3)>0:
                                                    if len(input_option_4)>0:
                                                        if radio_option == 'A' or radio_option == 'B' or radio_option == 'C' or radio_option == 'D':
                                                            code=200
                                                            lst.append(code)
                                                            msg=''
                                                            lst.append(msg)
                                                        else:
                                                            code=300
                                                            lst.append(code)
                                                            msg='Sorry! No option was selected...'
                                                            lst.append(msg)
                                                    else:
                                                        code=300
                                                        lst.append(code)
                                                        msg='Sorry! Option (D) field was empty...'
                                                        lst.append(msg)
                                                else:
                                                    code=300
                                                    lst.append(code)
                                                    msg='Sorry! Option (C) field was empty...'
                                                    lst.append(msg)
                                            else:
                                                code=300
                                                lst.append(code)
                                                msg='Sorry! Option (B) field was empty...'
                                                lst.append(msg)
                                        else:
                                            code=300
                                            lst.append(code)
                                            msg='Sorry! Option (A) field was empty...'
                                            lst.append(msg)
                                    else:
                                        code=200
                                        lst.append(code)
                                        msg=""
                                        lst.append(msg)
                                else:
                                    code=300
                                    lst.append(code)
                                    msg='Sorry! Answer field was empty...'
                                    lst.append(msg)
                            else:
                                code=300
                                lst.append(code)
                                msg='Sorry! Question field was empty...'
                                lst.append(msg)
                        else:
                            code=300
                            lst.append(code)
                            msg='Sorry! Question Type option was empty...'
                            lst.append(msg)
                    else:
                        code=300
                        lst.append(code)
                        msg='Sorry! Subject option was empty...'
                        lst.append(msg)
                else:
                    code=300
                    lst.append(code)
                    msg='Sorry! Standard option was empty...'
                    lst.append(msg)
            else:
                code=300
                lst.append(code)
                msg='Sorry! Board option was empty...'
                lst.append(msg)
        else:
            code=300
            lst.append(code)
            msg='Sorry! Language option was empty...'
            lst.append(msg)
    else:
        code=300
        lst.append(code)
        msg='Sorry! Category option was empty...'
        lst.append(msg)

    return lst

def submit_gta_form(request,input_category,input_language,input_board,input_standard,input_subject,input_qtype,input_question,radio_option,input_option_1,input_option_2,input_option_3,input_option_4,input_answer,form_status,qid):

    # field for sending form status
    fields={}

    # validating form
    validate=validate_gta_questions(input_category,input_language,input_board,input_standard,input_subject,input_qtype,input_question,radio_option,input_option_1,input_option_2,input_option_3,input_option_4,input_answer)

    if validate[0] == 300:
        fields['code']=300
        fields['msg']=validate[1]
    
    elif validate[0]==200:

        if form_status == 'new':

            if input_qtype == 'MCQ':
                try:
                    last_id=gta_all_question.objects.last().sno
                    form_values=gta_all_question(id=f"GTA0{last_id+1}",question_category=input_category,
                                                language=input_language,
                                                board=input_board,
                                                standard=input_standard,
                                                subject=input_subject,
                                                qtype=input_qtype,
                                                question=input_question, 
                                                option_1=input_option_1,option_2=input_option_2,option_3=input_option_3,option_4=input_option_4,answer_option=radio_option,
                                                answer=input_answer,
                                                user_profile=request.user)
                    form_values.save()
                    fields['code']=200
                    fields['msg']='Congratulations! Question saved successfuly...'

                except Exception:
                    fields['code']=300
                    fields['msg']='Failed! An error ocured. Please try again...'

            elif input_qtype == 'STQ' or input_qtype == 'LTQ' or input_qtype == 'VLTQ':
                try:
                    last_id=gta_all_question.objects.last().sno
                    form_values=gta_all_question(id=f"GTA0{last_id+1}",question_category=input_category,
                                                language=input_language,
                                                board=input_board,
                                                standard=input_standard,
                                                subject=input_subject,
                                                qtype=input_qtype,
                                                question=input_question,
                                                answer_option='Other',
                                                answer=input_answer,
                                                user_profile=request.user)
                    form_values.save()
                    fields['code']=200
                    fields['msg']='Congratulations! Question saved successfuly...'

                except Exception:
                    fields['code']=300
                    fields['msg']='Failed! An error ocured. Please try again...'
        # for updating questions
        elif form_status == 'old':
            question_sno=gta_all_question.objects.filter(id=qid).first().sno

            if input_qtype == 'MCQ':
                try:
                    form_values=gta_all_question(sno=question_sno,id=qid,question_category=input_category,
                                                language=input_language,
                                                board=input_board,
                                                standard=input_standard,
                                                subject=input_subject,
                                                qtype=input_qtype,
                                                question=input_question, 
                                                option_1=input_option_1,option_2=input_option_2,option_3=input_option_3,option_4=input_option_4,answer_option=radio_option,
                                                answer=input_answer,
                                                user_profile=request.user)
                    form_values.save()
                    fields['code']=200
                    fields['msg']='Congratulations! Question updated successfuly...'

                except Exception:
                    fields['code']=300
                    fields['msg']='Failed! An error ocured. Please try again...'

            elif input_qtype == 'STQ' or input_qtype == 'LTQ' or input_qtype == 'VLTQ':
                try:
                    form_values=gta_all_question(sno=question_sno,id=qid,question_category=input_category,
                                                language=input_language,
                                                board=input_board,
                                                standard=input_standard,
                                                subject=input_subject,
                                                qtype=input_qtype,
                                                question=input_question,
                                                answer_option='Other',
                                                answer=input_answer,
                                                user_profile=request.user)
                    form_values.save()
                    fields['code']=200
                    fields['msg']='Congratulations! Question updated successfuly...'

                except Exception:
                    fields['code']=300
                    fields['msg']='Failed! An error ocured. Please try again...'
            

    return fields


# function to write questions in database
# def write_questions(language,standard,subject,qtype):
#     old_questions=gurkul_academic_test_series_model.objects.filter(language=language,test_class=standard,subject=subject,qtype=qtype).all()

#     print(old_questions)

#     for item in old_questions:
#         new_questions=gta_all_question(question_category='Acad',language=language,standard=10,subject=subject,qtype=qtype,question=item.question,option_1=item.option_1,option_2=item.option_2,option_3=item.option_3,option_4=item.option_4,answer=item.answer,answer_option='Other',user_profile=item.user_profile)
#         new_questions.save()


# code for correcting data

    # test_ob=gta_all_question.objects.filter(question_category='Acad',language='Hindi',board='UPBoard',standard='12',subject='Physics',qtype='LTQ')

    # for item in test_ob:
    #     que= gta_all_question(sno=item.sno,id=item.id,question_category=item.question_category,language=item.language,board=item.board,standard=12,subject=item.subject,qtype=item.qtype,question=item.question,option_1=item.option_1,option_2=item.option_2,option_3=item.option_3,option_4=item.option_4,answer=item.answer,answer_option=item.answer_option,user_profile=item.user_profile,time=item.time)
    #     que.save()

    # print(test_ob)
    # print(len(test_ob))