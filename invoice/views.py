from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. request handler

def say_hello(request):
    print(request)
    return HttpResponse('Hola Mundo')
def show_response(request):
    x = 1
    y = 2 
    print(request)
    return render(request,'index.html',{'name':'Juan'})

def show_products(request):
    
    return render(request,'inventory/product.html',)
