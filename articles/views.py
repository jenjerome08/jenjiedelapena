from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Gclassroom, StudentInfo
from django.contrib.auth.decorators import login_required
from . import forms

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
@login_required(login_url="/accounts/login/")
def student_page(request):
    if request.method == 'POST':
        student = StudentInfo.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            section=request.POST['section'],
            age=request.POST['age'], 
            tupc_id=request.POST['tupc_id'],
            gender=request.POST['gender'],
            image=request.FILES['image']
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
    return render(request, 'articles/info_create.html')
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
