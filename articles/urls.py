from django.conf.urls import url
from . import views
#from django.urls import path
app_name = 'articles'

urlpatterns = [
    url(r'^$', views.task_list, name="list"),
    url(r'^create/$', views.task_create, name="create"),
    url(r'^(?P<task>[\w-]+)/$', views.task_detail, name="detail"),
    #Attendance
    url(r'^attendance_page/$', views.attendance_page, name="attendance_page"),
    url(r'^attendance_page/list$', views.attendance_list, name="attendance_list"),

    #StudentInfo
    url(r'^student_page/$', views.student_page, name="student_page"),
    url(r'^student_page/(?P<section>[\w-]+)/$', views.student_detail, name="studentdetail"),
    url(r'^student_page/studentlist$', views.student_list, name="student_list"),


    #Quiz
    url(r'^quiz_page/$', views.quiz_page, name="quiz_page"),
    url(r'^quiz_page/(?P<title>[\w-]+)/$', views.quiz_detail, name="quizdetail"),
    url(r'^quiz_page/quizlist$', views.quiz_list, name="quiz_list"),

    #url(r'^about/$', views.quiz, name="quiz"),
    #url(r'^info_detail/(?P<slugs>[\w-]+)/$', views.info_detail, name="info_detail"),
    #url(r'^info_create/$', views.info_create, name="info_create"),
]
