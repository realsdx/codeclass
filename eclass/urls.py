from django.urls import path
from eclass import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('home/student/', views.student_home, name="student-home" ),

]