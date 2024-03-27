from django.test import TestCase

import json
import requests

# Create your tests here.
URL = "http://127.0.0.1:8000/createmanager/"
data ={
    'name':'giri',
    'address':'hyd',
    'mail':'giri@gmail.com',
    'age':25
}
jsondata = json.dumps(data)
r = requests.get(url=URL, data=jsondata)
emp_data = r.json()
print(emp_data)
