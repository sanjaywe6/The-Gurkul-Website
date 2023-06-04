from datetime import date
from email.policy import default
from django.db import models
from sqlalchemy import true
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

# model for branch profile
class branch_profile(models.Model):
    sno=models.AutoField(primary_key=True)
    branch_code=models.CharField(max_length=20)
    branch_mgr=models.CharField(max_length=50,default="")
    branch_mgr_mob=models.BigIntegerField(default=0)
    branch_add=models.CharField(max_length=200)
    date=models.DateTimeField(default=now)

    def __str__(self):
        return self.branch_code+" ~ "+self.branch_add



# model for separate branch teacher
class branch_teacher_faculty(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    mob=models.BigIntegerField(default=0)
    msg_mob=models.BigIntegerField(default=0)
    sub=models.CharField(max_length=30)
    branch_code=models.CharField(max_length=20)
    date=models.DateTimeField(default=now)

    def __str__(self):
        return self.name+" ~ "+self.branch_code

