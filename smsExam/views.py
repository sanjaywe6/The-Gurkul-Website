from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from thegurkul.the_gurkul_functions import *
from smsExam.models import *
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