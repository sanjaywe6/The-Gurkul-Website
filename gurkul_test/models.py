from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class gurkul_academic_test_series_model(models.Model):
    sno=models.AutoField(primary_key=True)
    test_class=models.CharField(max_length=10,default="")
    board=models.CharField(max_length=30,default='')
    subject=models.CharField(max_length=30,default="")
    qtype=models.CharField(max_length=50,default="")
    language=models.CharField(max_length=30,default='Hindi')
    question=models.CharField(max_length=1000,default="")
    acad_q_1=models.CharField(max_length=100,default="")
    acad_q_2=models.CharField(max_length=100,default="")
    acad_q_3=models.CharField(max_length=100,default="")
    acad_q_4=models.CharField(max_length=100,default="")
    answer=models.CharField(max_length=5000,default="")
    user_profile=models.ForeignKey(User,on_delete=models.PROTECT,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.question[0:50]+"...."


class gurkul_competition_test_series_model(models.Model):
    sno=models.AutoField(primary_key=True)
    exam_type=models.CharField(max_length=50,default='')
    subject=models.CharField(max_length=30,default="")
    qtype=models.CharField(max_length=50,default="")
    language=models.CharField(max_length=30,default='Hindi')
    question=models.CharField(max_length=1000,default="")
    option_1=models.CharField(max_length=100,default="")
    option_2=models.CharField(max_length=100,default="")
    option_3=models.CharField(max_length=100,default="")
    option_4=models.CharField(max_length=100,default="")
    answer=models.CharField(max_length=5000,default="")
    user_profile=models.ForeignKey(User,on_delete=models.PROTECT,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.question[0:50]+"...."