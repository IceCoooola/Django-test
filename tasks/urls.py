<<<<<<< HEAD

app_name = "tasks"
urlpatterns = [
=======
from django.urls import path
from . import views

app_name = "tasks"


urlpatterns = [
    path('', views.task_list, name = 'task_list'),
>>>>>>> 45ecfd5a54504b81b1bfbf9b43cbfdd1f40486f4
]