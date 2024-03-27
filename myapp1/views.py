from django.shortcuts import render
from django.http import HttpResponse
from .import forms

# Create your views here.
def studentview(request):
    form = forms.StudentForm
    myform = {'form':form}
    return render(request,"home.html",context=myform)
