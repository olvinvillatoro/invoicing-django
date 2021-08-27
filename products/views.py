from products.models import Products
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductsSerializers


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    exampleProduct = {
        'name' : 'Pastilla',
        'price' : '100',
        'qtty' : '10',
        'descr' : 'Test product',
    }
    return Response(exampleProduct)

@api_view(['GET'])
def products(request):
    products = Products.objects.all()
    serializer = ProductsSerializers(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request,id):
    products = Products.objects.get(id=id)
    serializer = ProductsSerializers(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request,id):
    product = Products.objects.get(id=id)
    serializer = ProductsSerializers(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request,id):
    product = Products.objects.get(id=id)
    product.delete()
    return Response("Product deleted")