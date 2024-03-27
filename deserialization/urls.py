from django.contrib import admin
from django.urls import path
from deserialization import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createmanager/',views.create_manager),
    
]