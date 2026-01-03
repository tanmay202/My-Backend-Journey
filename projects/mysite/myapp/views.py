from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myView(reqest):
    return HttpResponse("Hello This is Me,Tanmay")

def Suburl(reques):
    return HttpResponse("This is sub url")