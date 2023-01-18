from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

# model for adding academic test series questions
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

# modal for adding competition test series questions
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

# modal for adding available test series options for students of academic
class all_academic_available_test_series(models.Model):
    sno=models.AutoField(primary_key=True)
    test_class=models.CharField(max_length=10,default="")
    subject=models.CharField(max_length=30,default="")
    language=models.CharField(max_length=30,default='Hindi')
    board=models.CharField(max_length=30,default='')
    test_type=models.CharField(max_length=50,default="model")
    img=models.ImageField(upload_to='img/gurkul_test/academic_available_test_series')
    user_profile=models.ForeignKey(User,on_delete=models.PROTECT,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.test_class+" "+self.board+" "+self.language+" "+self.subject

# modal for adding available test series options for students of competition
class all_competition_available_test_series(models.Model):
    sno=models.AutoField(primary_key=True)
    exam_type=models.CharField(max_length=10,default="")
    subject=models.CharField(max_length=30,default="")
    language=models.CharField(max_length=30,default='Hindi')
    test_type=models.CharField(max_length=50,default="model")
    img=models.ImageField(upload_to='img/gurkul_test/competition_available_test_series')
    user_profile=models.ForeignKey(User,on_delete=models.PROTECT,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.exam_type+" "+self.language+" "+self.subject