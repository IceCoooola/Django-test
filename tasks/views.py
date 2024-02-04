# from django.shortcuts import render
# from .models import Task
#
# # Create your views here.
#
# def task_list(request):
#     ## task_list, 用于展示任务清单。该视图函数从数据库读取了Task对象列表，指定了渲染模板并向模板传递了数据。
#
#     #从数据库获取Task 对象列表
#     tasks = Task.objects.all()
#     # 指定渲染模板并向模板传递数据
#     return render(request, "tasks/task_list.html", {"tasks": tasks,})
