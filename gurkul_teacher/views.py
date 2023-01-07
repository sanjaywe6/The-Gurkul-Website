from django.shortcuts import redirect, render
from django.http import JsonResponse
from gurkul_admin.models import *
from gurkul_teacher.models import *
from thegurkul.the_gurkul_functions import *

# Create your views here.

# function to deliver teacher profile
def teacher_profile(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)

    if user_type=='teacher' or user_type=='superuser':
        # getting techer id and filtering either profile exist or not
        teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
        profile_data=teacher_profile_data.objects.filter(teacher_id=teacher_id)
        if len(profile_data)>0:
            profile_data_existence="True"
            edit_profile_status='old'
        else:
            profile_data_existence="False"
            edit_profile_status='new'
        param={'profile_data_existence':profile_data_existence,'edit_profile_status':edit_profile_status,"profile_data":profile_data}
        return render(request,'gurkul_teacher/teacher_profile/teacher_profile_home.html',param)

    else:
        return redirect("/")

# function to edit teacher profile
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
        subject=request.POST.get('subject')
        addr=request.POST.get('addr')
        state=request.POST.get('state')
        city=request.POST.get('city')
        zip=request.POST.get('zip')
        bio=request.POST.get('bio')

        if load_old_profile_data=="true":
            teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
            profile_data=teacher_profile_data.objects.filter(teacher_id=teacher_id).values()
            profile_data=list(profile_data)
            return JsonResponse({'code':200,'profile_data':profile_data})

        # setting up users firstname and last name
        user_profile=User.objects.get(username=request.user)
        user_profile.first_name=fname
        user_profile.last_name=lname
        # getting teacher id
        teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
        if user_type=='teacher' or user_type=='superuser':
            if data_status=="new":
                profiel_data=teacher_profile_data(teacher_id=teacher_id,fname=fname,lname=lname,mob=mob,wmob=wmob,subject=subject,address=addr,state=state,city=city,zip=zip,bio=bio,user_profile=request.user)
                profiel_data.save()
                return JsonResponse({'code':200,'msg':'Congrates, Your profile data has been saved.....'})
            elif data_status=='old':
                teacher_sno=teacher_profile_data.objects.filter(teacher_id=teacher_id)[0].sno
                profiel_data=teacher_profile_data(sno=teacher_sno,teacher_id=teacher_id,fname=fname,lname=lname,mob=mob,wmob=wmob,subject=subject,address=addr,state=state,city=city,zip=zip,bio=bio,user_profile=request.user)
                profiel_data.save()
                return JsonResponse({'code':200,'msg':'Congrates, Your profile data has been saved.....'})
    else:
        if user_type=='teacher' or user_type=='superuser':
            # getting techer id and filtering either profile exist or not
            teacher_id=all_usrs.objects.filter(username=request.user)[0].teacher_id
            profile_data=teacher_profile_data.objects.filter(teacher_id=teacher_id)
            if len(profile_data)>0:
                profile_data_existence="True"
                edit_profile_status='old'
            else:
                profile_data_existence="False"
                edit_profile_status='new'
            
            param={'profile_data_existence':profile_data_existence,'edit_profile_status':edit_profile_status}
            return render(request,'gurkul_teacher/teacher_profile/edit_profile.html',param)

