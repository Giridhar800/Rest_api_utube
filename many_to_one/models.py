from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(max_length=20)
    post_catagery = models.CharField(max_length=30)
    publish_date =models.DateField()
