from django.urls import path, include
from accounts import views as v
# from app.views import TaskList,TaskDetial,CreateTask
urlpatterns = [
    # path('',include('django.contrib.auth.urls'),name='authurls'),
    path('login/',v.Login.as_view(),name='login'),
    path('logout/',v.Logout.as_view(),name='logout'),
    path('register/',v.Register.as_view(),name='register'),
]

