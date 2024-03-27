from django.shortcuts import render
from .models import Employee
from .serializers import EmpSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def emp_details(request,pk):
    emp = Employee.objects.get(id=pk)
    serializers = EmpSerializers(emp)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type='application/json')

def emp_all_details(request):
    emp = Employee.objects.all()
    serializers = EmpSerializers(emp,many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type='application/json')