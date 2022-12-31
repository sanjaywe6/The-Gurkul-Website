from django.shortcuts import redirect, render

# Create your views here.
def teacher_profile(request):
    return render(request,'gurkul_teacher/index.html')