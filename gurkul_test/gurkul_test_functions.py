from gurkul_test.models import *
import random

def get_form_optioins():
    options={}
    # getting question id
    id=gta_all_question.objects.last().sno
    options['id']=f"GTA0{id+1}"
    # getting cotegory
    category=question_category_choices
    options['category']=category
    # getting language
    languages=language_choices
    options['language']=languages
    # getting board
    boards=board_choices
    options['board']=boards
    # getting standard
    standards=standard_choices
    options['standard']=standards
    # getting subjects
    subjects=subject_choices
    options['subject']=subjects
    # getting question types
    qtypes=qtype_choices
    options['qtype']=qtypes
    # getting answer choices
    answer_options=answer_option_choices
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

def get_gta_modals(request):
    category=question_category_choices
    modal_index=0
    for cat in category:
        language=language_choices
        for lang in language:
            boards=board_choices
            for board in boards:
                standard=standard_choices
                for stand in standard:
                    subject=subject_choices
                    for subj in subject:
                        qtypes=qtype_choices
                        for qtype in qtypes:
                            modal=gta_all_question.objects.filter(question_category=cat[0],language=lang[0],board=board[0],standard=stand[0],subject=subj[0],qtype=qtype[0])
                            lent=len(modal)
                            if lent>50:
                                
                                # os.makedirs(f'static/theGurkul/img/gurkul_test/test_modal_banner/{cat[0]}/{lang[0]}/{board[0]}/{stand[0]}/{subj[0]}/{qtype[0]}')

                                modal_id=f'GTA00{modal_index}'
                                add_to_series=gta_test_series(id=modal_id,question_category=cat[0],language=lang[0],board=board[0],standard=stand[0],subject=subj[0],qtype=qtype[0],total_length=lent,banner=f"../static/theGurkul/img/gurkul_test/test_modal_banner/{cat[0]}_{lang[0]}_{board[0]}_{stand[0]}_{subj[0]}_{qtype[0]}.jpg")
                                add_to_series.save()
                                modal_index=modal_index+1

def get_gta_questions_for_given_question_id(id):
    questions={}
    modal=gta_test_series.objects.filter(id=id).first()
    questions=gta_all_question.objects.filter(question_category=modal.question_category,language=modal.language,board=modal.board,standard=modal.standard,subject=modal.subject,qtype=modal.qtype).values()
    random_questions=random.sample([x for x in questions],modal.questions_length)
    return random_questions