from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.task_list, name="list"),
    url(r'^create/$', views.task_create, name="create"),
    url(r'^(?P<task>[\w-]+)/$', views.task_detail, name="detail"),
    #Attendance
    url(r'^student_page/$', views.student_page, name="student_page"),
    #url(r'^info_detail/(?P<slugs>[\w-]+)/$', views.info_detail, name="info_detail"),
    #url(r'^info_create/$', views.info_create, name="info_create"),
]
