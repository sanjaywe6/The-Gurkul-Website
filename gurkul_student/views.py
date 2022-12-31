from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def student_profile(request):
    return render(request,'gurkul_student/student_profile/student_profile_home.html')

#  function for editing profiles of student
def edit_profile(request):
    return render(request,'gurkul_student/student_profile/edit_profile.html')

#  join gurkul form for users
def join_gurkul(request):
    return render(request,'gurkul_student/student_profile/join_gurkul.html')

#  page for complete profile of user
def complete_profile(request):
    return render(request,'gurkul_student/student_profile/complete_profile.html')