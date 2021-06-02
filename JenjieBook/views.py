from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')

def student_info(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
