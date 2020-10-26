from django.db import models


class Collegetb(models.Model):
    deptid=models.IntegerField()
    deptname=models.CharField(max_length=256)
    depthod=models.CharField(max_length=256)
    location=models.CharField(max_length=256)



