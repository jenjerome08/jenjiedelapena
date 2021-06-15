from django import forms
from . import models
from .models import Attendance, StudentInfo, CreateQuiz, Attendance, Gclassroom

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Gclassroom
        fields = ['subject', 'body', 'task', 'image', 'file',]

class CreateAttendance(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = ['day', 'time', 'date', 'in_and_out',]

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentInfo
        fields = ['first_name', 'last_name', 'section', 'age', 'tupc_id', 'gender', 'image',]

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.CreateQuiz
        fields = [
        'title',
        'Q1', 'a1', 'b1', 'c1', 'd1',
        'Q2', 'a2', 'b2', 'c2', 'd2',
        'Q3', 'a3', 'b3', 'c3', 'd3',
        'Q4', 'a4', 'b4', 'c4', 'd4',
        ]