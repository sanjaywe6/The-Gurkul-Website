from django.shortcuts import redirect, render

# Create your views here.
def gurkul_admin_index(request):
    return render(request,'gurkul_admin/index.html')