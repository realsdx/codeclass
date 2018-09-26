from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

def student_home(req):
    return render(req,'eclass/student_home.html', {})

def index(req):
    return render(req,'eclass/index.html', {})
