# models.py in the 'main' app
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
