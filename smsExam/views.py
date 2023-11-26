from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from thegurkul.the_gurkul_functions import *
from smsExam.models import *
from gurkul_teacher.models import *
import random
from . import smsExam_functions


# Create your views here.

def student_registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        std_class = request.POST.get('std_class')
        aadhar = request.POST.get('aadhar')
        mob = request.POST.get('mob')
        wmob = request.POST.get('wmob')
        subject = request.POST.get('subject')
        institution = request.POST.get('institution')
        addr = request.POST.get('addr')

        img = request.FILES.get('img')

        captcha_value = request.POST.get('captcha_value')
        captcha_id = request.POST.get('captcha_id')

        db_data_std = studentRegistration.objects.last()
        new_uin_num = db_data_std.sno+1

        # verifying captcha
        captcha_val = captcha_verification(captcha_id, captcha_value)

        if captcha_val == 'True':
            submit_student_form = smsExam_functions.submit_std_reg_form(fname,lname,dob,email,father,mother,std_class,aadhar,mob,wmob,subject,institution, addr, captcha_value, captcha_id, new_uin_num, img)

        else: 
            submit_student_form = {'code':300,'msg':'Sorry Captcha Verification failed..'}

        return JsonResponse({'submit_student_form':submit_student_form})
    else:
        captcha=random.choice(captcha_data.objects.all())
        param={'captcha':captcha}
        return render(request, 'student_registration.html',param)
    
def all_student_data(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)
    if user_type=='teacher':
            teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
            auth_to_edit_data=teacher_auth.objects.filter(teacher_id=teacher_id).first().edit_sms_exam_student_data
            if auth_to_edit_data==True:
                student_data = studentRegistration.objects.all()
                param = {'student_data':student_data}
                return render(request, 'all_student_data.html',param)
            else:
                return render(request, 'all_student_data_unauthorized.html')
    else:
        return render(request, 'all_student_data_unauthorized.html')
    
    

def student_data_with_sno(request,sno):

    # verifying usertype
    user_type=gurkul_user_type(request.user)
    if user_type=='teacher':
        teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
        auth_to_edit_data=teacher_auth.objects.filter(teacher_id=teacher_id).first().edit_sms_exam_student_data
        if auth_to_edit_data==True:
            if request.method == 'POST':
                std_data = request.POST.get('std_data')
                std_data_type = request.POST.get('std_data_type')

                get_std = studentRegistration.objects.filter(sno = sno).first()
                if std_data_type == 'fname' and len(std_data)>0:
                    get_std.fname = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'lname' and len(std_data)>0:
                    get_std.lname = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'father_name' and len(std_data)>0:
                    get_std.father_name = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'mother_name' and len(std_data)>0:
                    get_std.mother_name = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'email' and len(std_data)>0:
                    get_std.email = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'mob' and len(std_data)>0:
                    get_std.mob = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'wmob' and len(std_data)>0:
                    get_std.wmob = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'dob' and len(std_data)>0:
                    get_std.dob = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'aadhar' and len(std_data)>0:
                    get_std.aadhar = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'std_class' and len(std_data)>0:
                    get_std.std_class = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'subject' and len(std_data)>0:
                    get_std.subject_class = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'institution' and len(std_data)>0:
                    get_std.institution = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')
                elif std_data_type == 'addr' and len(std_data)>0:
                    get_std.addr = std_data
                    get_std.save()
                    messages.add_message(request,50,'Congratulations ! Data updated successfuly...')

                else:
                    messages.add_message(request,40,'Sorry ! Data updation failed...')

                student_data = studentRegistration.objects.filter(sno = sno).first()
                param = {'student_data':student_data}
                return render (request, 'student_data_with_sno.html', param)
            else:
                student_data = studentRegistration.objects.filter(sno = sno).first()
                param = {'student_data':student_data}
                return render (request, 'student_data_with_sno.html', param)
        
        else:
            return render(request,'all_student_data_unauthorized.html')
    