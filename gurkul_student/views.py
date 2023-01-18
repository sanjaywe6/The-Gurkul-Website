from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from thegurkul.the_gurkul_functions import *
from gurkul_student.models import *
from django.http import JsonResponse

# Create your views here.
# function to deliver student profile
def student_profile(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)

    if user_type=='student' or user_type=='superuser':
        # getting techer id and filtering either profile exist or not
        student_id=all_usrs.objects.filter(username=request.user)[0].student_id
        profile_data=student_profile_data.objects.filter(student_id=student_id)
        if len(profile_data)>0:
            profile_data_existence="True"
            edit_profile_status='old'
        else:
            profile_data_existence="False"
            edit_profile_status='new'
        param={'profile_data_existence':profile_data_existence,'edit_profile_status':edit_profile_status,"profile_data":profile_data,'student_id':student_id}
        return render(request,'gurkul_student/student_profile/student_profile_home.html',param)

    else:
        return redirect("/")

# function to edit student profile
def edit_profile(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)
    if request.method=='POST':
        # getting data from page
        load_old_profile_data=request.POST.get('load_old_profile_data')
        data_status=request.POST.get('data_status')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mob=request.POST.get('mob')
        wmob=request.POST.get('wmob')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        pmob=request.POST.get('wmob')
        addr=request.POST.get('addr')
        state=request.POST.get('state')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        bio=request.POST.get('bio')

        # sending profile data if profile already exist
        if load_old_profile_data=="true":
            student_id=all_usrs.objects.filter(username=request.user)[0].student_id
            profile_data=student_profile_data.objects.filter(student_id=student_id).values()
            profile_data=list(profile_data)
            return JsonResponse({'code':200,'profile_data':profile_data})

        # setting up users firstname and last name
        user_profile=User.objects.get(username=request.user)
        user_profile.first_name=fname
        user_profile.last_name=lname
        user_profile.save()

        # getting student id
        student_id=all_usrs.objects.filter(username=request.user)[0].student_id
        if user_type=='student' or user_type=='superuser':
            # if recive data is new
            if data_status=="new":
                profiel_data=student_profile_data(student_id=student_id,fname=fname,lname=lname,mob=mob,wmob=wmob,father_name=father_name,mother_name=mother_name,pmob=pmob,address=addr,state=state,city=city,zip=zip,bio=bio,user_profile=request.user)
                profiel_data.save()
                return JsonResponse({'code':200,'msg':'Congrates, Your profile data has been saved.....'})
            # 
            elif data_status=='old':
                student_sno=student_profile_data.objects.filter(student_id=student_id)[0].sno
                profiel_data=student_profile_data(sno=student_sno,student_id=student_id,fname=fname,lname=lname,mob=mob,wmob=wmob,father_name=father_name,mother_name=mother_name,pmob=pmob,address=addr,state=state,city=city,zip=zip,bio=bio,user_profile=request.user)
                profiel_data.save()
                return JsonResponse({'code':200,'msg':'Congrates, Your profile data has been saved.....'})
    else:
        if user_type=='student' or user_type=='superuser':
            # getting techer id and filtering either profile exist or not
            student_id=all_usrs.objects.filter(username=request.user)[0].student_id
            profile_data=student_profile_data.objects.filter(student_id=student_id)
            if len(profile_data)>0:
                profile_data_existence="True"
                edit_profile_status='old'
            else:
                profile_data_existence="False"
                edit_profile_status='new'
            
            param={'profile_data_existence':profile_data_existence,'edit_profile_status':edit_profile_status,'student_id':student_id}
            return render(request,'gurkul_student/student_profile/edit_profile.html',param)
        
        else:
            return redirect("/")

#  join gurkul form for users
def join_gurkul(request):
    return render(request,'gurkul_student/student_profile/join_gurkul.html')
