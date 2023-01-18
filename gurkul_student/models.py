from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
# modal adding teacher profile data
class student_profile_data(models.Model):
    sno=models.AutoField(primary_key=True)
    student_id=models.CharField(max_length=20,default="")
    fname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    mob=models.CharField(max_length=20,default="")
    wmob=models.CharField(max_length=20,default="")
    father_name=models.CharField(max_length=50,default="")
    mother_name=models.CharField(max_length=50,default="")
    pmob=models.CharField(max_length=20,default="")
    address=models.CharField(max_length=500,default="")
    state=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    zip=models.CharField(max_length=100,default="")
    bio=models.CharField(max_length=1000,default="")
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,default="")

    def __str__(self) -> str:
        return self.fname+"~"+self.lname+"~"+self.student_id