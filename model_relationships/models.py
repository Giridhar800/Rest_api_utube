from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    # user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})

    bname = models.CharField(max_length=20)
    bauthor = models.CharField(max_length=20)
    bpublishdate = models.DateField()
