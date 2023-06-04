from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from thegurkul.the_gurkul_functions import *
from gurkul_student.models import *
from django.http import JsonResponse
from . import gurkul_student_functions

# Create your views here.
# function to deliver student profile
def student_profile(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)

    student_id=all_usrs.objects.filter(username=request.user)[0].student_id
    if user_type=='student' or user_type=='superuser':

        # loading data of student educational profile
        educational_data=student_educational_profile_data.objects.filter(student_id=student_id).all()

        # getting techer id and filtering either profile exist or not
        profile_data=student_profile_data.objects.filter(student_id=student_id)

        # dictionar data to send on student profile page
        param={'profile_data_existence':gurkul_student_functions.profile_data_existance(student_id),'edit_profile_status':gurkul_student_functions.edit_profile_status(student_id),"profile_data":profile_data,'student_id':student_id,'educational_data_existence':gurkul_student_functions.educational_data_existence(student_id),'educational_data':educational_data}
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

        # getting student id
        student_id=all_usrs.objects.filter(username=request.user)[0].student_id

        # sending profile data if profile already exist
        if load_old_profile_data=="true":
            profile_data=student_profile_data.objects.filter(student_id=student_id).values()
            profile_data=list(profile_data)
            return JsonResponse({'code':200,'profile_data':profile_data})

        # setting up users firstname and last name
        user_profile=User.objects.get(username=request.user)
        user_profile.first_name=fname
        user_profile.last_name=lname
        user_profile.save()

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
            
            param={'profile_data_existence':profile_data_existence,'edit_profile_status':edit_profile_status,'student_id':student_id,'educational_data_existence':gurkul_student_functions.educational_data_existence(student_id)}
            return render(request,'gurkul_student/student_profile/edit_profile.html',param)
        
        else:
            return redirect("/")

#function to edit educational profile
def edit_educational_profile(request):
    # verifying usertype
    user_type=gurkul_user_type(request.user)

    # getting student id
    student_id=all_usrs.objects.filter(username=request.user)[0].student_id

    if request.method=='POST':

        # variable to know that either it is requested old data or new data
        educational_data_status=request.POST.get('educational_data_status')

        # getting value of data_field number by which we can determine that which data needs to be editted
        sno=request.POST.get('sno')

        # student submitted form data
        data_field=request.POST.get('data_field')
        standard=request.POST.get('standard')
        stream=request.POST.get('stream')
        college=request.POST.get('college')
        board=request.POST.get('board')
        roll_no=request.POST.get('roll_no')
        maximum_marks=request.POST.get('maximum_marks')
        obtained_marks=request.POST.get('obtained_marks')
        marks_percent=request.POST.get('percent')
        year=request.POST.get('year')

        # verifying usertype and further adding/updating data in database
        if user_type=='student' or user_type=='superuser':
            # if recived data is new
            if educational_data_status=="new":
                educational_data=student_educational_profile_data(student_id=student_id,data_field=data_field,standard=standard,stream=stream,college=college,board=board,roll_no=roll_no,maximum_marks=maximum_marks,obtained_marks=obtained_marks,marks_percent=marks_percent,year=year,user_profile=request.user)

                educational_data.save()
                return JsonResponse({'code':200,'msg':'Congrates, Your profile data has been saved.....','data_field':data_field})

            # if recieved is old
            elif educational_data_status=='old':
                id=student_educational_profile_data.objects.filter(student_id=student_id,data_field=sno)[0].sno
                educational_data=student_educational_profile_data(sno=id,student_id=student_id,data_field=data_field,standard=standard,stream=stream,college=college,board=board,roll_no=roll_no,maximum_marks=maximum_marks,obtained_marks=obtained_marks,marks_percent=marks_percent,year=year,user_profile=request.user)
                educational_data.save()
                return JsonResponse({'code':200,'msg':'Congrates, Your profile data has been saved.....','data_field':data_field})



        

        # variable to know either gotten profile data is new or old for database
        educational_data_status=request.POST.get('educational_data_status')


        # variable to get that which data is submitted, either it is new data or old data
        data_status=request.POST.get('data_status')

        # variable to know that when add more educational profile is clicked then which slot is empty for education profile
        data_field_for_empty_slots=request.POST.get('data_field_for_empty_slots')
        # logic for sending empty slot
        if data_field_for_empty_slots == 'True':
            data_field_num=gurkul_student_functions.data_field_empty_slot(student_id)
            return JsonResponse({'code':200,'data_field_num':data_field_num})


    else:
        if user_type=='student' or user_type=='superuser':

            # if student has already any educational profile then sending it data true
            educational_data=student_educational_profile_data.objects.filter(student_id=student_id)
            if len(educational_data)>0:
                educational_data_existence="True"
            else:
                educational_data_existence="False"
            
            param={'educational_data_existence':educational_data_existence,'student_id':student_id,'educational_data_type':'new','profile_data_existence':gurkul_student_functions.profile_data_existance(student_id)}

            return render(request,'gurkul_student/student_profile/edit_educational_profile.html',param)
        
        else:
            return redirect("/")

def load_old_educational_profile(request):
    student_id=all_usrs.objects.filter(username=request.user)[0].student_id
    if request.method=='POST':
        sno=request.POST.get('sno')
        # code to know that when need to render to educational form or when needs to send student old data
        render_to_educational_form=request.POST.get('render_to_educational_form')
        if render_to_educational_form == 'True':
            sno_educational_data=student_educational_profile_data.objects.filter(student_id=student_id,data_field=sno)
            if len(sno_educational_data)>0:
                param={'sno':sno,'educational_data_type':'old','student_id':student_id,'profile_data_existence':gurkul_student_functions.profile_data_existance(student_id)}
                return render(request,'gurkul_student/student_profile/edit_educational_profile.html',param)

        else:
            # sending old profile data to student
            profile=student_educational_profile_data.objects.filter(data_field=sno,student_id=student_id).values()
            profile=list(profile)
            return JsonResponse({'code':200,'profile':profile})

#  join gurkul form for users
def join_gurkul(request):
    return render(request,'gurkul_student/student_profile/join_gurkul.html')
