from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.

@api_view(['POST'])
def createProduct(request):
    if request.method == "POST":
        serializer =  ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getProducts(request):
    if request.method == "GET":
        product = Product.objects.all()
        serializer = ProductSerializer(product, context = {"request": request}, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


