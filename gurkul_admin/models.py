from email.policy import default
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.timezone import now
from sqlalchemy import null

# Create your models here.

#  The Gurkul app models

# creating contact message database
class contact_us(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=70,default="")
    visitor_type=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=1000,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.name+"~"+self.desc[0:50]


# model for landing page home slide image
class landing_home_page_slide(models.Model):
    sno=models.AutoField(primary_key=True)
    about=models.CharField(max_length=200,default="")
    img=models.ImageField(upload_to='img/gurkul_admin/home/landing_home_page_slide')
    time=models.DateTimeField(default=now)

    def __str__(self):
        return self.about
    
# model for teacher faculty image 
class teacher_faculty(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40,default="")
    about=models.CharField(max_length=50,default="")
    quote=models.CharField(max_length=1000,default="")
    img=models.ImageField(upload_to="img/gurkul_admin/home/teacher_faculty")

    def __str__(self):
        return self.name+" ~ "+self.about

#  Models for student registration
class all_usrs(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=40,null=False)
    passwd=models.CharField(max_length=100,null=False,default='')
    branch_code=models.CharField(max_length=20,null=True,default="")
    student_id=models.CharField(max_length=20,null=True,default="")
    teacher_id=models.CharField(max_length=20,null=True,default="")
    visitor_type=models.CharField(max_length=40,null=False)
    userProfile=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.username+" ~ "+self.visitor_type

#  Models for all superuser registration
class gurkul_all_superuser(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=40,null=False)
    passwd=models.CharField(max_length=100,null=False,default='')
    admin_id=models.CharField(max_length=20,null=True,default="")
    visitor_type=models.CharField(max_length=40,null=False)
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.username+" ~ "+self.user_type

# model for getting number of visitors on website
class vistor_count(models.Model):
    sno=models.AutoField(primary_key=True)
    ip=models.CharField(max_length=30,default="")
    time=models.TimeField(default=now)

    def __str__(self):
        return self.ip


# model for captcha verification
class captcha_data(models.Model):
    sno=models.AutoField(primary_key=True)
    first_character=models.CharField(max_length=1,default="")
    second_character=models.CharField(max_length=1,default="")
    value=models.CharField(max_length=4,default="")

    def __str__(self):
        return self.value

