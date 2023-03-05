from gurkul_test.models import *

def write_questions(category,language,standard,subject,qtype):
    if (category=='comp'):
        old_questions=gurkul_competition_test_series_model.objects.filter(language=language,exam_type=standard,subject=subject,qtype=qtype).all()
        
        for item in old_questions:
            new_questions=gta_all_question(question_category='Comp',language=language,standard=standard,subject=subject,qtype=qtype,question=item.question,option_1=item.option_1,option_2=item.option_2,option_3=item.option_3,option_4=item.option_4,answer=item.answer,user_profile=item.user_profile)
            new_questions.save()

