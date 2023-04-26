from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class gta_all_question(models.Model):
    sno=models.AutoField(primary_key=True)
    id=models.CharField(max_length=15,default="GTA00")

    # category choices question means either Academic or Competition
    question_category_choices=(
        ('Acad','Academic'),
        ('Comp','Competition'),
        ('Other','Other'),
    )
    question_category=models.CharField(choices=question_category_choices,max_length=20,default='Other')

    # language options
    language_choices=(
        ('Hindi','Hindi'),
        ('English','English'),
        ('Other','Other'),
    )
    language=models.CharField(choices=language_choices,max_length=30,default='Other')

    # Board Options
    board_choices=(
        ('UPBoard','UP Board'),
        ('Other','Other'),
    )
    board=models.CharField(choices=board_choices,max_length=50,default='Other')

    # standard available choices 
    standard_choices=(
        ('10','10th'),
        ('11','11th'),
        ('12','12th'),
        ('NEET','National Eligibility cum Entrance Test (NEET)'),
        ('SSC','Staff Selection Commission'),
        ('Banking','Banking'),
        ('UPP/UPSI','UPP/UP Police SI'),
        ('Other','Other'),
    )
    standard=models.CharField(choices=standard_choices,max_length=50,default="Other")

    # all available choice for subjects
    subject_choices=(
        ('Mathematics','Mathematics'),
        ('Science','Science'),
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ('Biology','Biology'),
        ('Geography','Geography'),
        ('Reasoning','Reasoning'),
        ('GS/GK','General Science (GS) / General Knowledge (GK)'),
        ('History','History'),
        ('Hindi','Hindi'),
        ('Other','Other'),
    )
    subject=models.CharField(choices=subject_choices,max_length=30,default="Other")

    # question type choice that means mcq, msq etc.
    qtype_choices=(
        ('MCQ','Multiple Choice Question (MCQ)'),
        ('STQ','Short Type Question (STQ)'),
        ('LTQ','Long Type Question (LTQ)'),
        ('VLTQ','Very Long Type Question (VLTQ)'),
        ('Other','Other'),
    )
    qtype=models.CharField(choices=qtype_choices,max_length=50,default="Other")

    question=models.TextField()
    question_img=models.ImageField(upload_to='img/gurkul_test/all_questions/%y/%m/%d/question',default="")

    option_1=models.CharField(max_length=100,default="")
    option_1_img=models.ImageField(upload_to='img/gurkul_test/all_questions/%y/%m/%d/option_1',default="")

    option_2=models.CharField(max_length=100,default="")
    option_2_img=models.ImageField(upload_to='img/gurkul_test/all_questions/%y/%m/%d/option_2',default="")

    option_3=models.CharField(max_length=100,default="")
    option_3_img=models.ImageField(upload_to='img/gurkul_test/all_questions/%y/%m/%d/option_3',default="")

    option_4=models.CharField(max_length=100,default="")
    option_4_img=models.ImageField(upload_to='img/gurkul_test/all_questions/%y/%m/%d/option_4',default="")

    answer=models.TextField(max_length=5000,default="")
    answer_img=models.ImageField(upload_to='img/gurkul_test/all_questions/%y/%m/%d/answer',default="")


    # optional answer choice either A, B, C or D
    answer_option_choices=(
        ('A','Option A'),
        ('B','Option B'),
        ('C','Option C'),
        ('D','Option D'),
        ('Other','Other'),
        )
    answer_option=models.CharField(choices=answer_option_choices,max_length=10,default="Other")

    user_profile=models.ForeignKey(User,on_delete=models.PROTECT,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.question_category+"~"+self.question[0:70]+"...."
