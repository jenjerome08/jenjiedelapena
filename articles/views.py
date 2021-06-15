from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gclassroom, StudentInfo, Attendance, CreateQuiz
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CreateAttendance, CreateTask, StudentForm, QuizForm

def quiz(request):
    return render(request, 'articles/quiz.html')
#TASK
def task_list(request):
    tasks = Gclassroom.objects.all().order_by('subject');
    return render(request, 'articles/task_list.html', { 'tasks': tasks })

def task_detail(request, task):
    taskmo = Gclassroom.objects.get(task=task)
    return render(request, 'articles/task_detail.html', { 'taskmo': taskmo })

@login_required(login_url="/accounts/login/")
def task_create(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateTask()
    return render(request, 'articles/task_create.html', { 'form': form })

#ATTENDANCE
def attendance_list(request):
    attends = Attendance.objects.all().order_by('date');
    return render(request, 'articles/info_list.html', { 'attends': attends })
def attendance_detail(request, attend):
    attendmo = Attendance.objects.get(attend=attend)
    return render(request, 'articles/info_detail.html', { 'attendmo': attendmo })
@login_required(login_url="/accounts/login/")
def attendance_page(request):
    if request.method == 'POST':
        form = forms.CreateAttendance(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('articles:attendance_list')

    form = forms.CreateAttendance()
    return render(request, 'articles/info_create.html', { 'form': form })
#STUDENTINFO
def student_list(request):
    jenjies = StudentInfo.objects.all().order_by('last_name');
    return render(request, 'articles/studentlist.html', { 'jenjies': jenjies })
def student_detail(request, section):
    jenjiemo = StudentInfo.objects.get(section=section)
    return render(request, 'articles/studentdetail.html', { 'jenjiemo': jenjiemo })
@login_required(login_url="/accounts/login/")
def student_page(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('articles:student_list')
    form = forms.StudentForm()
    return render(request, 'articles/studentcreate.html', { 'form': form })
#QUIZZ
def quiz_list(request):
    quizes = CreateQuiz.objects.all().order_by('title');
    return render(request, 'articles/quizlist.html', { 'quizes': quizes })
def quiz_detail(request, title):
    quizmo = CreateQuiz.objects.get(title=title)
    return render(request, 'articles/quizdetail.html', { 'quizmo': quizmo })

@login_required(login_url="/accounts/login/")
def quiz_page(request):
    if request.method == 'POST':
        form = forms.QuizForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = request.user
            instance.save()
            return redirect('articles:quiz_list')
    form = forms.QuizForm()
    return render(request, 'articles/quizcreate.html', { 'form': form })




'''def info_list(request):
    infos = StudentInfo.objects.all().order_by('subject');
    return render(request, 'articles/info_list.html', { 'infos': infos })'''

'''def info_detail(request, slug):
    infomo = Gclassroom.objects.get(slugs=slugs)
    return render(request, 'articles/info_detail.html', { 'infomo': infomo })
def info_create(request):
    if request.method == 'POST':
        student = StudentInfo.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            section=request.POST['section'],
            age=request.POST['age'], 
            tupc_id=request.POST['tupc_id'],
            gender=request.POST['gender'],
            image=request.POST['image']
            )
        obj = StudentInfo()
        obj.first_name = first_name
        obj.last_name = last_name
        obj.section = section
        obj.age = age
        obj.tupc_id = tupc_id
        obj.gender = gender
        obj.image = image
        obj.save()
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('articles:info_list')
    else:
        student = StudentInfo.objects.create()
    return render(request, 'articles/info_create.html', {'obj': obj})'''
