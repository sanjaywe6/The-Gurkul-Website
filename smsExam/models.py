from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
from decimal import Decimal
from django.utils import timezone
# Create your models here.

class_choices = {
    ('9','Nine (9th)'),
    ('10','Ten (10th)'),
    ('11','Eleven (11th)'),
    ('12','Twelve (12th)'),
    ('Other','Other'),
}

subject_choices = {
    ('Mathematics','Mathematics'),
    ('Biology','Biology'),
    ('Other','Other'),
}

class studentRegistration(models.Model):
    sno = models.AutoField(primary_key=True)
    uin_no = models.CharField(max_length=11, default="GTASMS0")
    img = models.ImageField(upload_to='img/smsExam/%Y/%m')
    fname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    email = models.EmailField(null=True)
    mob=models.CharField(max_length=20,default="")
    wmob=models.CharField(max_length=20,default="")
    father_name=models.CharField(max_length=50,default="")
    mother_name=models.CharField(max_length=50,default="")
    dob = models.DateField(default='2000-01-01')
    aadhar = models.CharField(max_length=13, default='0000 0000 0000')
    std_class = models.CharField(choices=class_choices, max_length=10, default='Other')
    subject_class = models.CharField(choices=subject_choices, max_length=20, default='Other')
    institution = models.CharField(max_length=100, default='The Gurkul')
    addr = models.CharField(max_length=100, default='Bahraich')
    time = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.uin_no+"~"+self.fname+" "+self.lname