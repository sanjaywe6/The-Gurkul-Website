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
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.fname+"~"+self.lname+"~"+self.student_id

# model for student educational deatails
class student_educational_profile_data(models.Model):
    sno=models.AutoField(primary_key=True)
    student_id=models.CharField(max_length=20,default="")
    data_field=models.IntegerField()
    standard=models.CharField(max_length=20,default="")
    stream=models.CharField(max_length=20,default="")
    college=models.CharField(max_length=100,default="")
    board=models.CharField(max_length=100,default="")
    roll_no=models.CharField(max_length=20,default="")
    maximum_marks=models.IntegerField()
    obtained_marks=models.IntegerField()
    marks_percent=models.CharField(max_length=10,default="")
    year=models.CharField(max_length=10,default="")
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.student_id+"~"+self.standard+"~"+self.board

paper_attempt_status_choices=(
    ('Yes','Completed'),
    ('No','Not Completed'),
)
class student_test_paper_data(models.Model):
    sno=models.AutoField(primary_key=True)
    paper_id=models.CharField(max_length=20,default='')
    attempt=models.IntegerField(default=0)
    attempt_status=models.CharField(choices=paper_attempt_status_choices,default='No',max_length=10)
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    time=models.DateTimeField(default=now)
    
    def __str__(self) -> str:
        return self.user_profile+'~'+self.paper_id+'~'+self.attempt_status
