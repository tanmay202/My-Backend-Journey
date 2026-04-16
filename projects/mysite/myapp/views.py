from django.http import HttpResponse
from .models import Item
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def myView(reqest):
    return render(reqest,"myapp/index.html")

def Suburl(reques):
    return HttpResponse("This is sub url")

def HomePage(reques):
    return HttpResponse("<h1>This is the home page</h1>")

@login_required 
def DataBase(request):
    my_item=Item.objects.all()
    context={
        'my_item':my_item
    }
    return render(request,'myapp/index.html',context)

# def detail(request,id):
#     item=Item.objects.get(id=id)

  

#     context={
#         'item':item
#     }
#     return render(request,'myapp/detail.html',context)

def detail(request, id):
    item = get_object_or_404(Item, id=id)

    context = {
        'item': item
    }
    return render(request, 'myapp/detail.html', context)


def create_item(request):
    if request.method=='POST':
        form=ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('db')
    else:
         form=ItemForm()
    context={
        'form':form
    }
    return render(request,'myapp/item-form.html',context)


#update item view:

def update_item(request,id):
    item = get_object_or_404(Item, id=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
            form.save()
            return redirect('db')
    context={
        'form':form
    }

    return render(request,'myapp/item-form.html',context)

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('db')

    return render(request, 'myapp/itemdel.html', {'item': item})

