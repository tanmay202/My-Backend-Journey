from django.shortcuts import render
from django.http import HttpResponse
from .models import Myclass
# Create your views here.


def PracticeView(req):
    _list=Myclass.objects.all()
    return HttpResponse(_list) 
