from django.urls import path
from .views import *

urlpatterns = [
    path('api/',Booklist),
    path('add/',Book_post),
    path('update/<int:id>/',update_book),
    path('del/<int:id>/',delete_book),
]