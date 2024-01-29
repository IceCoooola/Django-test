from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    #从数据库获取Task 对象列表
    tasks = Task.objects.all()
    