from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    age=models.PositiveBigIntegerField()
    bio=models.CharField(max_length=256)
