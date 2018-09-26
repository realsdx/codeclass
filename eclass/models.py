from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    classes = models.CharField(max_length=512, null=True, blank=True) #Store a json list of class ids

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    class_enrolled = models.CharField(max_length=256, default="DONT USE THIS") #NE=NotEnrolled
    qs_assigned = models.CharField(max_length=256, default="NA") #NA=NotAssigned
    ans_submited = models.CharField(max_length=256, default="NS") #NS=NoneSubmited
    total_score = models.FloatField(default=0.00)

    def __str__(self):
        return self.name


class Problem(models.Model):
    """This hold all types of Problems, including custom ones, a teacher can add to it."""
    problem_statement = models.TextField(blank=True, null=True)
    problem_uri = models.URLField(blank=True, null=True)

class Assignment(models.Model):
    """This model only represents each assignment given to a student"""
    title = models.CharField(max_length=256)
    question = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

    submission = models.TextField(blank=True, null=True)
    is_submited = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='media/',null=True, blank=True)
    due_by = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class CodeClass(models.Model):
    class_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ManyToManyField(Student, blank=True)
    qs_list = models.CharField(max_length=512, blank=True, null=True) #Store a json list of qs/assignment ids


    def __str__(self):
        return self.class_name



