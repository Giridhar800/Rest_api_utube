from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import pdb;pdb.set_trace();


# Create your views here.
# Read
@api_view(['GET'])
def Booklist(request):
   
    booksobj = BooksModel.objects.all()
    serializer = BookSerializers(booksobj,many=True)
    return Response(serializer.data)

# Create
@api_view(['POST'])
def Book_post(request):
    booksobj = BooksModel.objects.all()
    serializer = BookSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Update
@api_view(['POST'])
def update_book(request, id):
    booksobj = BooksModel.objects.get(id=id)
    serializer = BookSerializers(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Delete
@api_view(['DELETE'])
def delete_book(request, id):
    booksobj = BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response("Book is deleted")