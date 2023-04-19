"""
URL configuration for logic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from tasks import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^tasks/(?P<pk>\d+)/$', views.task_questions, name='task_questions'),
    re_path(r'^tasks/(?P<pk>\d+)/delete/$', views.delete_task, name='delete_task'),
    re_path(r'^tasks/(?P<pk>\d+)/new_q_logic/$', views.new_q_logic, name='new_q_logic'),
    re_path(r'^tasks/(?P<pk>\d+)/new_q_choose_option/$', views.new_q_choose_option, name='new_q_choose_option'),
    re_path(r'^tasks/(?P<pk>\d+)/q_logic/(?P<q_logic_pk>\d+)$', views.edit_q_logic, name='edit_q_logic'),
    re_path(r'^tasks/(?P<pk>\d+)/q_logic/(?P<q_logic_pk>\d+)/delete/$', views.delete_q_logic, name='delete_q_logic'),
    re_path(r'^tasks/(?P<pk>\d+)/q_choose_option/(?P<q_choose_option_pk>\d+)$', views.edit_q_choose_option, name='edit_q_choose_option'),
    re_path(r'^tasks/(?P<pk>\d+)/q_choose_option/(?P<q_choose_option_pk>\d+)/delete/$', views.delete_q_choose_option, name='delete_q_choose_option'),
    re_path(r'^admin/', admin.site.urls),
    ]
