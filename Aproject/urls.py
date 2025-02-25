"""
URL configuration for Aproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from students import views
from newbook import views

urlpatterns = [
    path('admin/',admin.site.urls),
    # path('api/',views.StudentList.as_view()),
    # path('add/',views.StudentCreate.as_view()),
    # path('display/<int:pk>/',views.Studentrev.as_view()),
    # path('update/<int:pk>/',views.StudentrUp.as_view()),
    # path('delete/<int:pk>/',views.StudentrDel.as_view()),
    # path('lc/',views.StudentLC.as_view()),
    # path('ru/<int:pk>/',views.StudentRU.as_view()),
    # path('rd/<int:pk>/',views.StudentRD.as_view()),
    # path('rud/<int:pk>/',views.StudentRUD.as_view()),
    
    path('book1/',include('newbook1.urls')),
    path('myapp1/',include('myapp1.urls')),
    path('',include('book.urls')),
    path('ser/',include('serializers.urls')),
    path('dser/',include('deserialization.urls')),
    path('a/',include('functionbasedview.urls')),
]
