from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def myView(reqest):
    return render(reqest,"myapp/index.html")

def Suburl(reques):
    return HttpResponse("This is sub url")

def HomePage(reques):
    return HttpResponse("<h1>This is the home page</h1>")


def DataBase(request):
    my_item=Item.objects.all()
    context={
        'my_item':my_item
    }
    return render(request,'myapp/index.html',context)

def detail(request,id):
    item=Item.objects.get(id=id)
    context={
        'item':item
    }
    return render(request,'myapp/detail.html',context)