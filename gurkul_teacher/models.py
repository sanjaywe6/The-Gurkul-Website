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
    edit_test_series=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.teacher_username+"~ "+self.teacher_id