from rest_framework import serializers
from .models import Manager

class ManagerSerializers(serializers.Serializer):
    # class Meta:
    #     model = Employee
    #     fields = '__all__'
    
    ename = serializers.CharField(max_length=20)
    eaddress = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    def create(self, validated_data):
        return Manager.objects.create(**validated_data)