from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser 
from functionbasedview.serializers import EmployeeSerializers
from .models import Employee
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import pdb;pdb.set_trace();

# Create your views here.
@csrf_exempt
def emp_data(request):
    if request.method == 'GET':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializers(emp)
            jsondata = JSONRenderer().render(serializer.data)
            return HttpResponse(jsondata,content_type='application/json')
        emp = Employee.objects.all()
        serializer = EmployeeSerializers(emp,many=True)
        jsondata = JSONRenderer().render(serializer.data)
        return HttpResponse(jsondata,content_type='application/json')



    if request.method == 'POST':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        serializer = EmployeeSerializers(data = py_data)
        if serializer.is_valid():
            serializer.save()
            result ={'message':'data inserted into database'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata,content_type='application/json')
        
        jsondata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
    

    if request.method == 'PUT':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializers( emp,data = py_data)
        if serializer.is_valid():
            serializer.save()
            result ={'message':'data updated into database'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata,content_type='application/json')
        
        jsondata = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')
    

    if request.method == 'DELETE':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete
        result = {'message':'data deleted from data base'}
        
        jsondata = JSONRenderer().render(result)
        return HttpResponse(jsondata,content_type='application/json')
        
        


