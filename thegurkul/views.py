from pydoc import describe
import re
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from gurkul_admin.models import *
from gurkul_teacher.models import *
from django.http import JsonResponse
from . import the_gurkul_functions
import random


#  function for home page
def home(request):

    visitor_ip=the_gurkul_functions.get_client_ip_address(request)

    visitor_data_update=vistor_count(ip=visitor_ip)
    visitor_data_update.save()

    teachers=teacher_faculty.objects.all()
    num=len(teachers)
    intro_slide_img=landing_home_page_slide.objects.all()
    param={'teachers':teachers,'len':num,'intro_slide_img':intro_slide_img}
    return render(request,'home.html',param)

# function to give total visitor from database
def total_visitor(request):
    if request.method=='GET':
        total_visitors=str(len(vistor_count.objects.all()))
        visitor_num_list=[x for x in total_visitors]
        while len(visitor_num_list)<6:
            visitor_num_list.insert(0,'0')
        return JsonResponse({'data':visitor_num_list})


#  function for about page
def about(request):
    return render(request,'about.html')

#  function for contact page
def contact(request):
    if request.method=="POST":
        # getting contact form data from page
        name=request.POST.get('inputName')
        email=request.POST.get('inputEmail')
        vtype=request.POST.get('Vtype')
        desc=request.POST.get('desc')

        # getting captcha value for verification 
        captcha_value=request.POST.get('captcha_value')
        captcha_id=request.POST.get('captcha_id')
        result=the_gurkul_functions.captcha_verification(captcha_id,captcha_value)
        if result=="True":
            contact_db=contact_us(name=name,email=email,visitor_type=vtype,desc=desc)
            contact_db.save()
            messages.add_message(request,50,'Dear, Your querry has been sent..')
        else:
            messages.add_message(request,50,'Sorry! Invalid captcha found...')
    captcha=random.choice(captcha_data.objects.all())
    param={'captcha':captcha}
    return render(request,'contact.html',param)

#  function for handling go to profile
def user_profile(request):
    user=all_usrs.objects.filter(userProfile=request.user)
    usertype=user[0].visitor_type
    if usertype=='student':
        return redirect('/gurkul_student/student_profile/')
    elif usertype=='gurkul_branch':
        return redirect('/gurkul_branch/branch_profile/')
    elif usertype=='teacher':
        return redirect('/gurkul_teacher/teacher_profile/')
    elif usertype=='superuser':
        return redirect('/gurkul_administration/admin_index/')
    else:
        messages.add_message(request,50,'Some Internal Error Found')
        return redirect('/')

# function for user registration
def usrRegistration(request):
    if request.method=='POST':
        username=request.POST.get('inputUsername')
        email=request.POST.get('inputEmail')
        passwd=request.POST.get('inputPassword')
        passwdc=request.POST.get('inputPasswordC')
        usertype=request.POST.get('usertype')

        # getting captcha value for verification 
        captcha_value=request.POST.get('captcha_value')
        captcha_id=request.POST.get('captcha_id')
        result=the_gurkul_functions.captcha_verification(captcha_id,captcha_value)
        if result=="True":

            # check the username
            # check username length
            if len(username)>5:
                #  check special char in username
                special_char=["[","@",",","_","-","!","$","%","^","&","*","(",")","<",">","?","/","|","{","}","~",":","]","#","(",")","=","+"," "]
                special_char_bool=False
                for item in special_char:
                    if item in username:
                        special_char_bool=True
                if special_char_bool==False:
                    # check whether username exist or not
                    user=all_usrs.objects.filter(username=username)
                    if len(user)==0:
                    # password verification
                        if len(passwd)>5:
                            if passwd==passwdc:
                                # creating user with username and password
                                create_user=User.objects.create_user(username,email,passwd)
                                #  authenticating user for login after registration
                                user=authenticate(username=username,password=passwd)

                                if user!=None:
                                    #  login user after registration
                                    login(request,user)

                                    # adding model related with user
                                    user_data=all_usrs(username=username,passwd=passwd,visitor_type=usertype,userProfile=request.user)
                                    user_data.save()
                                    # if registered usertype is gurkul_branch then adding data to all_users model
                                    if usertype=="gurkul_branch":
                                        branch=all_usrs.objects.filter(username=username)
                                        code=branch[0].sno
                                        branch_code=f"GSAB01{code}"
                                        user_data=all_usrs(sno=code,username=username,passwd=passwd,visitor_type=usertype,userProfile=request.user,branch_code=branch_code)
                                        user_data.save()
                                        return redirect('/gurkul_branch/branch_profile/')

                                    # if registered usertype is student then adding data to all_users model
                                    elif usertype=='student':
                                        student=all_usrs.objects.filter(username=username)
                                        id=student[0].sno
                                        student_id=f"GS001{id}"
                                        user_data=all_usrs(sno=id,username=username,passwd=passwd,visitor_type=usertype,userProfile=request.user,student_id=student_id)
                                        user_data.save()
                                        return redirect('/gurkul_student/student_profile/')

                                     # if registered usertype is teacher then adding data to all_users model
                                    elif usertype=='teacher':
                                        teacher=all_usrs.objects.filter(username=username)
                                        id=teacher[0].sno
                                        teacher_id=f"GT001{id}"
                                        user_data=all_usrs(sno=id,username=username,passwd=passwd,visitor_type=usertype,userProfile=request.user,teacher_id=teacher_id)
                                        user_data.save()
                                        #  saving data of teacher authorizations on web
                                        teacher_per=teacher_auth(teacher_id=teacher_id,teacher_username=username,user_profile=request.user)
                                        teacher_per.save()
                                        return redirect('/gurkul_teacher/teacher_profile/')

                                    else:
                                        messages.add_message(request,50,'Unknown Error Found While Sign Up! Please try again later.')
                                else:
                                    messages.add_message(request,50,'Unknown Error Found While Sign Up! Please try again later.')
                            else:
                                messages.add_message(request,50,'Both Passwords are not same.') 
                        else:
                            messages.add_message(request,50,'Password length must be greater than 5')
                    else:
                        messages.add_message(request,50,'This username is already taken, please try something different.')

                else:
                    messages.add_message(request,50,'Username can not containe special Charecters.')
            else:
                messages.add_message(request,50,'Username length must be greater than 6')
        else:
            messages.add_message(request,50,'Sorry! Invalid captcha found...')
            captcha=random.choice(captcha_data.objects.all())
            param={'captcha':captcha}
            return render(request,'usr_registration.html',param)

    captcha=random.choice(captcha_data.objects.all())
    param={'captcha':captcha}
    return render(request,'usr_registration.html',param)

# function for user login
def usrLogin(request):
    if request.method=="POST":
       username=request.POST.get('inputUsername') 
       password=request.POST.get('inputPassword')
       usertype=request.POST.get('usertype')

       # getting captcha value for verification 
       captcha_value=request.POST.get('captcha_value')
       captcha_id=request.POST.get('captcha_id')
       result=the_gurkul_functions.captcha_verification(captcha_id,captcha_value)
       if result=="True":
            # verify user with user type
          utype=all_usrs.objects.filter(username=username,visitor_type=usertype)
          if len(utype)==1:
                user=authenticate(username=username,password=password)
                if user!=None:
                    login(request,user)
                    if usertype=='student':
                        return redirect('/gurkul_student/student_profile/')
                    elif usertype=='gurkul_branch':
                        return redirect('/gurkul_branch/branch_profile/')
                    elif usertype=='teacher':
                        return redirect('/gurkul_teacher/teacher_profile/')
                    elif usertype=='superuser':
                        return redirect('/gurkul_administration/admin_index/')
                else:
                    messages.add_message(request,50,'Wrong user credentials! username or password is incorrect, Please try again..')
                    captcha=random.choice(captcha_data.objects.all())
                    param={'captcha':captcha}
                    return render(request,'usr_login.html',param)
          else:
            messages.add_message(request,50,'Wrong user credentials! username or password is incorrect, Please try again..')
            captcha=random.choice(captcha_data.objects.all())
            param={'captcha':captcha}
            return render(request,'usr_login.html',param)

       else:
          messages.add_message(request,50,'Sorry! Invalid captcha found...')
          captcha=random.choice(captcha_data.objects.all())
          param={'captcha':captcha}
          return render(request,'usr_login.html',param)

    else:
        captcha=random.choice(captcha_data.objects.all())
        param={'captcha':captcha}
        return render(request,'usr_login.html',param)

#  function for user logout
def usrLogout(request):
    logout(request)
    messages.add_message(request,30,'Logout Successful')
    return redirect('/')