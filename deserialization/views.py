from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from deserialization.serializers import ManagerSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt

def create_manager(request):
    if request.method == 'POST':
        jsondata = request.body
        stream = io.BytesIO(jsondata)
        py_data = JSONParser().parse(stream)
        serializer = ManagerSerializers(data=py_data)
        if serializer.is_valid():
            serializer.save()
            result = {'message':'data inserted into data base'}
            jsondata = JSONRenderer().render(result)
            return HttpResponse(jsondata,content_type = 'application/json')
        jsondata = JSONRenderer().render(serializer.errors)
    return HttpResponse(jsondata,content_type='application/json')
