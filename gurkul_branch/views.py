from django.shortcuts import redirect, render
from gurkul_admin.models import *
from gurkul_branch.models import *
# Create your views here.


def branch_index(request):
    user=all_usrs.objects.filter(userProfile=request.user)
    user_type=user[0].visitor_type
    branch_code=user[0].branch_code
    if user_type=="gurkul_branch" or user_type=='superuser':
        print('user authorize by branch code and visitor type')
        new_branch_profile=branch_profile.objects.filter(branch_code=branch_code).first()
        if new_branch_profile==None:
            print('Branch Profile data is empty')
            new_profile=branch_profile(branch_code=branch_code,branch_mgr='Unknown',branch_mgr_mob=0,branch_add='Unknown')
            new_profile.save()
        profile=branch_profile.objects.filter(branch_code=branch_code)
        param={'branch_code':branch_code,'profile':profile}
        return render(request,'gurkul_branch/branch_index.html',param)
    else:
        return redirect('/')

# function for updating branch profile
def update_branch_profile(request):
    if request.method=='POST':
        type=request.POST.get('type')
        data=request.POST.get('data')
        user=all_usrs.objects.filter(userProfile=request.user)
        user_type=user[0].visitor_type
        branch_code=user[0].branch_code
        if user_type=="gurkul_branch" or user_type=='superuser':
            profile=branch_profile.objects.filter(branch_code=branch_code).first()
            branch_mgr=profile.branch_mgr
            branch_mgr_mob=profile.branch_mgr_mob
            branch_add=profile.branch_add
            sno=profile.sno
            date=profile.date
            if type=='branch_mgr':
                update=branch_profile(sno=sno,branch_code=branch_code,branch_mgr=data,branch_mgr_mob=branch_mgr_mob,branch_add=branch_add,date=date)
                update.save()
            if type=='branch_mgr_mob':
                update=branch_profile(sno=sno,branch_code=branch_code,branch_mgr=branch_mgr,branch_mgr_mob=data,branch_add=branch_add,date=date)
                update.save()
            if type=='branch_add':
                update=branch_profile(sno=sno,branch_code=branch_code,branch_mgr=branch_mgr,branch_mgr_mob=branch_mgr_mob,branch_add=data,date=date)
                update.save()

        return redirect('/gurkul_branch/branch_profile/')
    else:
        return redirect('/')