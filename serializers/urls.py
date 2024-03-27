from django.contrib import admin
from django.urls import path
from serializers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/<int:pk>',views.emp_details),
    path('empall/',views.emp_all_details)
]