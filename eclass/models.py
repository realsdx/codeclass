from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Problems(models.Model):
    """This hold all types of Problems, including custom ones"""
    c_statement = models.TextField(blank=True, null=True)
    
    problem_uri = models.URLField(blank=True, null=True)

class Assignment(models.Model):
    question = models.TextField(blank=True, null=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_enrolled = models.CharField(max_length=256, default="NE") #NE=NotEnrolled
    qs_assigned = models.CharField(max_length=256, default="NA") #NA=NotAssigned
    ans_submited = models.CharField(max_length=256, default="NS") #NS=NoneSubmited

