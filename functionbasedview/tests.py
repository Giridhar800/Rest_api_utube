from django.test import TestCase


import json
import requests

# Create your tests here.
URL = "http://127.0.0.1:8000/emp/"

def get_record(id = None):
    data = {}
    if id is not None:
        data = {'id':id }
        jsondata = json.dumps(data)
        r = requests.get(url = URL, data=jsondata)
        data = r.json
        print(data)
# get_record()
# get_record(1)

def post_record():
    data ={
    'name':'giri',
    'address':'hyd',
    'mail':'giri@gmail.com',
    'age':25
}
    jsondata = json.dumps(data)
    r = requests.get(url=URL, data=jsondata)
    data = r.json()
    print(data)
post_record()


def update_record():
    data ={
        'id':1,
    'name':'giri',
    'address':'hyd',
    'mail':'giri@gmail.com',
    'age':25
}
    jsondata = json.dumps(data)
    r = requests.put(url=URL, data=jsondata)
    data = r.json()
    print(data)
# update_record()


def delete_record():
    data ={
        'id':1}
    jsondata = json.dumps(data)
    r = requests.delete(url=URL, data=jsondata)
    data = r.json()
    print(data)
# delete_record()



