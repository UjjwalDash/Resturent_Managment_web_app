from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,filepath

# Create your views here.
def book(request):
    return render(request,'index.html')
def add(request):
    return render(request,'add.html')
def update_price(request):
    return render(request,'update_price.html')
def update_image(request):
    return render(request,'update_image.html')
def delete(request):
    return render(request,'delete.html')
def show(request):
    return render(request,'show.html')

    
def success(request):
    return HttpResponse('successfully uploaded')




def insert(request):
    prod=Item()
    prod.food_name=request.GET['food_name']
    prod.food_price=request.GET['food_price']
    prod.food_image=request.FILES['food_image']
    print(prod.food_image)
    
    prod.save()
    return render(request,'add.html')
    
    