from rest_framework import serializers
from .models import Employee

class EmpSerializers(serializers.Serializer):
    # class Meta:
    #     model = Employee
    #     fields = '__all__'
    id = serializers.CharField(max_length=20)
    ename = serializers.CharField(max_length=20)
    eaddress = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=20)
