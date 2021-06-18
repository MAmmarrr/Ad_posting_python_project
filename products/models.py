from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(null=False,blank=True)
    category = models.CharField(max_length=255,null=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=400)
    users = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posted",null=True)
