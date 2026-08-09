from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.
def First(request):
    item=Item.objects.all()
    context={
        'item_list':item
    }
    return render(request,"myapp/1.html",context)

def detail(request,id):
    item=Item.objects.get(id=id)
    context={
        'item':item
    }
    return render(request,"myapp/detail.html",context)
