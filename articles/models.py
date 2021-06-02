from django.db import models
from django.contrib.auth.models import User

class StudentInfo(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    slugs = models.SlugField()
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    
    SECTION_CHOICES = (
        ('BSIE-ICT-3A', 'BSIE-ICT-3A'),
        ('BSIE-ICT-3B', 'BSIE-ICT-3B'),
    )
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, null=True)
    age = models.IntegerField(blank=True, null=True)
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
    image = models.ImageField(default='default.png', blank=True)
    

    def __str__(self):
        return self.subject

    def snippet(self):
        return self.body[:100] + '...'
class Attendance(models.Model):
    #student = models.ManyToManyField(StudentUser, blank=True )
    students = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=50, default="", null=True)
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
    field_name = models.DateField(auto_now=False, auto_now_add=False,)

    IN_OUT = (
        ('In', 'Check-In'),
        ('Out', 'Check-Out'),

    )
    in_and_out = models.CharField(max_length=50, choices=IN_OUT, null=True)

    def __str__(self):
        
        return self.student_attendance
