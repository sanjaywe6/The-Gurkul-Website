from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
from decimal import Decimal

# Create your models here.

# category choices question means either Academic or Competition
question_category_choices=(
    ('Acad','Academic'),
    ('Comp','Competition'),
    ('Other','Other'),
    )
# language options
language_choices=(
    ('Hindi','Hindi'),
    ('English','English'),
    ('Other','Other'),
    )
# Board Options
board_choices=(
    ('UPBoard','UP Board'),
    ('Other','Other'),
    )
# standard available choices 
standard_choices=(
    ('10','10th'),
    ('11','11th'),
    ('12','12th'),
    ('NEET','National Eligibility cum Entrance Test (NEET)'),
    ('SSC','Staff Selection Commission'),
    ('Banking','Banking'),
    ('UPPorUPSI','UPP/UP Police SI'),
    ('TET','Teacher Eligibility Test (TET)'),
    ('CTET','Central Teacher Eligibility Test (CTET)'),
    ('STET','Secondary Teacher Eligibility Test (STET)'),
    ('PET','Preliminary Eligibility Test (PET)'),
    ('SSC_GD','Staff Selection Commision (SSC GD)'),
    ('SSC_MTS','Staff Selection Commision (SSC MTS)'),
    ('SSC_CGL','Staff Selection Commision (SSC CGL)'),
    ('PCS','Provincial Civil Service (PCS)'),
    ('UPSC','Union Public Service Commission (UPSC)'),
    ('PRT','Primary teacher (PRT)'),
    ('KVS','Kendriya Vidyalaya Sangathan (KVS)'),
    ('TGT','Trained Graduate Teacher (TGT)'),
    ('PGT','Post-Graduate Teacher (PGT)'),
    ('NET','National Eligibility Test (NET)'),
    ('GATE','Graduate Aptitude Test in Engineering (GATE)'),
    ('UPSSSC','Uttar Pradesh Subordinate Services Selection Commission (UPSSSC)'),
    ('NDA','National Defence Academy (NDA)'),
    ('Air_Force','Air Force'),
    ('Navy','Navy'),
    ('Navy_SSR','Indian Navy Senior Secondary Recruit (Navy SSR)'),
    ('Other','Other'),
    )
# all available choice for subjects
subject_choices=(
    ('Mathematics','Mathematics'),
    ('Science','Science'),
    ('Physics','Physics'),
    ('Chemistry','Chemistry'),
    ('Biology','Biology'),
    ('Geography','Geography'),
    ('Reasoning','Reasoning'),
    ('GSorGK','General Science (GS) / General Knowledge (GK)'),
    ('History','History'),
    ('Hindi','Hindi'),
    ('Other','Other'),
    )
# question type choice that means mcq, msq etc.
qtype_choices=(
    ('MCQ','Multiple Choice Question (MCQ)'),
    ('STQ','Short Type Question (STQ)'),
    ('LTQ','Long Type Question (LTQ)'),
    ('VLTQ','Very Long Type Question (VLTQ)'),
    ('Other','Other'),
    )
# optional answer choice either A, B, C or D
answer_option_choices=(
    ('A','Option A'),
    ('B','Option B'),
    ('C','Option C'),
    ('D','Option D'),
    ('Other','Other'),
    )
class gta_all_question(models.Model):
    sno=models.AutoField(primary_key=True)
    id=models.CharField(max_length=15,default="GTA00")
    question_category=models.CharField(choices=question_category_choices,max_length=20,default='Other')
    language=models.CharField(choices=language_choices,max_length=30,default='Other')
    board=models.CharField(choices=board_choices,max_length=50,default='Other')
    standard=models.CharField(choices=standard_choices,max_length=50,default="Other")
    subject=models.CharField(choices=subject_choices,max_length=30,default="Other")
    qtype=models.CharField(choices=qtype_choices,max_length=50,default="Other")
    question=models.TextField()
    question_img=models.ImageField(upload_to='img/gurkul_test/all_questions/year_%Y/month_%m/day_%d/question',default="")
    option_1=models.CharField(max_length=100,default="")
    option_1_img=models.ImageField(upload_to='img/gurkul_test/all_questions/year_%Y/month_%m/day_%d/option_1',default="")
    option_2=models.CharField(max_length=100,default="")
    option_2_img=models.ImageField(upload_to='img/gurkul_test/all_questions/year_%Y/month_%m/day_%d/option_2',default="")
    option_3=models.CharField(max_length=100,default="")
    option_3_img=models.ImageField(upload_to='img/gurkul_test/all_questions/year_%Y/month_%m/day_%d/option_3',default="")
    option_4=models.CharField(max_length=100,default="")
    option_4_img=models.ImageField(upload_to='img/gurkul_test/all_questions/year_%Y/month_%m/day_%d/option_4',default="")
    answer=models.TextField(max_length=5000,default="")
    answer_img=models.ImageField(upload_to='img/gurkul_test/all_questions/year_%Y/month_%m/day_%d/answer',default="")
    answer_option=models.CharField(choices=answer_option_choices,max_length=10,default="Other")
    user_profile=models.ForeignKey(User,on_delete=models.PROTECT,default="")
    time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.question_category+"~"+self.question[0:70]+"...."

# Modal for all test series
test_series_reading_time_choices=(
    (timedelta(seconds=0),'0 Minutes'),
    (timedelta(seconds=300),'5 Minutes'),
    (timedelta(seconds=600),'10 Minutes'),
    (timedelta(seconds=900),'15 Minutes'),
    )
test_series_time_period_choices=(
    (timedelta(seconds=900),'15 Minutes'),
    (timedelta(seconds=1800),'30 Minutes'),
    (timedelta(seconds=2700),'45 Minutes'),
    (timedelta(seconds=3600),'1 Hour'),
    (timedelta(seconds=5400),'1.5 Hours'),
    (timedelta(seconds=7200),'2 Hours'),
    (timedelta(seconds=9000),'2.5 Hours'),
    (timedelta(seconds=10800),'3 Hours'),
    )
test_series_questions_length_choices=(
    (10,'10 Questions'),
    (15,'15 Questions'),
    (20,'20 Questions'),
    (25,'25 Questions'),
    (30,'30 Questions'),
    (35,'35 Questions'),
    (40,'40 Questions'),
    (45,'45 Questions'),
    (50,'50 Questions'),
    (55,'55 Questions'),
    (60,'60 Questions'),
    (65,'65 Questions'),
    (70,'70 Questions'),
    (75,'75 Questions'),
    (80,'80 Questions'),
    (85,'85 Questions'),
    (90,'90 Questions'),
    (95,'95 Questions'),
    (100,'100 Questions'),
    )
test_series_negative_marking_choices=(
    (Decimal('-0.50'),'-1/2 Markin per wrong answer'),
    (Decimal('-1.00'),'-1 Markin per wrong answer'),
    (Decimal('-1.50'),'-3/2 Markin per wrong answer'),
    (Decimal('-2.00'),'-2 Markin per wrong answer'),
)
test_series_positive_marking_choices=(
    (Decimal('0.50'),'1/2 Markin per right answer'),
    (Decimal('1.00'),'1 Markin per right answer'),
    (Decimal('1.50'),'3/2 Markin per right answer'),
    (Decimal('2.00'),'2 Markin per right answer'),
    (Decimal('2.50'),'5/2 Markin per right answer'),
    (Decimal('3.00'),'3 Markin per right answer'),
)
class gta_test_series(models.Model):
    sno=models.AutoField(primary_key=True)
    id=models.CharField(max_length=15,default=f'GTA0{sno}')
    question_category=models.CharField(choices=question_category_choices,max_length=20,default='Other')
    language=models.CharField(choices=language_choices,max_length=30,default='Other')
    board=models.CharField(choices=board_choices,max_length=50,default='Other')
    standard=models.CharField(choices=standard_choices,max_length=50,default="Other")
    subject=models.CharField(choices=subject_choices,max_length=30,default="Other")
    qtype=models.CharField(choices=qtype_choices,max_length=50,default="Other")
    total_length=models.IntegerField(default=0)
    reading_time=models.DurationField(choices=test_series_reading_time_choices,default=timedelta(minutes=30))
    time_period=models.DurationField(choices=test_series_time_period_choices,default=timedelta(minutes=30))
    questions_length=models.IntegerField(choices=test_series_questions_length_choices,default=15)
    negative_marking=models.DecimalField(max_digits=5,decimal_places=2,choices=test_series_negative_marking_choices,default=-1.00)
    positive_marking=models.DecimalField(max_digits=5,decimal_places=2,choices=test_series_positive_marking_choices,default=2.00)
    banner=models.ImageField(upload_to='img/gurkul_test/all_gta_test_modals/banners',default="")
    add_time=models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.question_category+'~'+self.language+'~'+self.board+'~'+self.standard+'~'+self.subject+'~'+self.qtype                 