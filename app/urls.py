from django.urls import path
from app import views as v
# from app.views import TaskList,TaskDetial,CreateTask
urlpatterns = [
    path('home',v.index,name='home'),
    path('tasks',v.TaskList.as_view(),name='tasklist'),
    path('task/<int:pk>',v.TaskDetial.as_view(),name='taskdetial'),
    path('create',v.CreateTask.as_view(),name='createtask'),
    path('update/<int:pk>',v.UpdateTask.as_view(),name='updatetask'),
    path('delete/<int:pk>',v.DeleteTask.as_view(),name='deletetask'),
]

