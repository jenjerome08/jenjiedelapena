from django.db import models
from django.contrib.auth.models import User

class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    MULTIPLE_CHOICES1 = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    answer1 = models.CharField(max_length=50, choices=MULTIPLE_CHOICES1, null=True)
    MULTIPLE_CHOICES2 = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    answer2 = models.CharField(max_length=50, choices=MULTIPLE_CHOICES2, null=True)
    MULTIPLE_CHOICES3 = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    answer3 = models.CharField(max_length=50, choices=MULTIPLE_CHOICES3, null=True)
    MULTIPLE_CHOICES4 = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    answer4 = models.CharField(max_length=50, choices=MULTIPLE_CHOICES4, null=True)

class CreateTask(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tasknumber = models.SlugField()
    announcement = models.TextField()
    startdate = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    upload_file = models.FileField(default='none', blank=True,)
class CreateQuiz(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.SlugField()
    Q1 = models.TextField(blank=True,default="")
    a1 = models.CharField(max_length=50, default="", blank=True)
    b1 = models.CharField(max_length=50, default="", blank=True)
    c1 = models.CharField(max_length=50, default="", blank=True)
    d1 = models.CharField(max_length=50, default="", blank=True)
    Q2 = models.TextField(blank=True,default="")
    a2 = models.CharField(max_length=50, default="", blank=True)
    b2 = models.CharField(max_length=50, default="", blank=True)
    c2 = models.CharField(max_length=50, default="", blank=True)
    d2 = models.CharField(max_length=50, default="", blank=True)
    Q3 = models.TextField(blank=True,default="")
    a3 = models.CharField(max_length=50, default="", blank=True)
    b3 = models.CharField(max_length=50, default="", blank=True)
    c3 = models.CharField(max_length=50, default="", blank=True)
    d3 = models.CharField(max_length=50, default="", blank=True)
    Q4 = models.TextField(blank=True,default="")
    a4 = models.CharField(max_length=50, default="", blank=True)
    b4 = models.CharField(max_length=50, default="", blank=True)
    c4 = models.CharField(max_length=50, default="", blank=True)
    d4 = models.CharField(max_length=50, default="", blank=True)
class StudentInfo(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    section = models.SlugField()
    age = models.IntegerField()
    tupc_id = models.CharField(max_length=50, default="")

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
# Create your models here.
class Gclassroom(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=100)
    task = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True,)
    file = models.FileField(default='none', blank=True,)
    

    def __str__(self):
        return self.subject

    def snippet(self):
        return self.body[:100] + '...'
class Attendance(models.Model):
    #student = models.ManyToManyField(StudentUser, blank=True )
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    day = models.CharField(max_length=50, choices=DAY_CHOICES, null=True)

    time = models.TimeField(auto_now=False, auto_now_add=False,)
    date = models.DateField(auto_now=False, auto_now_add=False,)

    IN_OUT = (
        ('Check-In', 'Check-In'),
        ('Check-Out', 'Check-Out'),

    )
    in_and_out = models.CharField(max_length=50, choices=IN_OUT, null=True)

    def __str__(self):
        
        return self.day
