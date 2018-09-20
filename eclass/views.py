from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

def home(req):
    return render(req,'eclass/home.html', {})

def index(req):
    return render(req,'eclass/index.html', {})
