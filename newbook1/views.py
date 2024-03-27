from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class Studentviewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Student.objects.all()
#         serializers = StudentSerializer(queryset,many=True)
#         return Response(serializers.data)
    
#     def retrieve(self,request,pk=None):
#         id=pk
#         if id is not None:
#             queryset = Student.objects.get(id=id)
#             serializers = StudentSerializer(queryset)
#             return Response(serializers.data)
        
#     def update(self,request,pk=None):
#         id=pk
#         queryset = Student.objects.get(pk=id)
#         serializers = StudentSerializer(queryset,data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'msg':"complete data updated"})
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self,request,pk=None):
#         id=pk
#         queryset = Student.objects.get(pk=id)
#         queryset.delete()
#         return Response({'msg':"deleted sucussfully..."})
    
#     def create(self,request):
#         serializers = StudentSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'msg':"complete data created..."})
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

# MODEL VIEW SET

class Studentviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
        
            
        
    
