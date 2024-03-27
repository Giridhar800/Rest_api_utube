from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.Serializer):
    ename = serializers.CharField(max_length=20)
    eaddress = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=20)
    age = serializers.IntegerField()


def create(self, validated_date):
    return Employee.objects.create(**validated_date)

def update(self,instance,validated_date):
    instance.name = validated_date.get('name',instance.name)
    instance.address = validated_date.get('address',instance.address)
    instance.email = validated_date.get('email',instance.email)
    instance.age = validated_date.get('age',instance.age)
    instance.save()
    return instance
