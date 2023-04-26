from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class teacher_auth(models.Model):
    sno=models.AutoField(primary_key=True)
    teacher_id=models.CharField(max_length=20,default="")
    teacher_username=models.CharField(max_length=50,default="")
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,default="")

    send_request_edit_test_series_choice=(
        ('none','Do Not Send The Request'),
        ('send','Send Request'),
        ('accept','Request Accepted'),
        ('decline','Request Declined'),
    )
    send_request_edit_test_series=models.CharField(choices=send_request_edit_test_series_choice,max_length=30,default="none")
    edit_test_series=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.teacher_id+"~"+self.teacher_username

# modal adding teacher profile data
class teacher_profile_data(models.Model):
    sno=models.AutoField(primary_key=True)
    teacher_id=models.CharField(max_length=20,default="")
    fname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    mob=models.CharField(max_length=20,default="")
    wmob=models.CharField(max_length=20,default="")
    subject=models.CharField(max_length=40,default="")
    address=models.CharField(max_length=500,default="")
    state=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    zip=models.CharField(max_length=100,default="")
    bio=models.CharField(max_length=1000,default="")
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,default="")

    def __str__(self) -> str:
        return self.fname+"~"+self.lname+"~"+self.teacher_id