from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task, name='task'),
    path('get-tasks/', views.getTasks, name='getTasks'),
    path('delete-task/', views.deleteTask, name='deleteTask'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
