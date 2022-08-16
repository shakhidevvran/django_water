from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    bottle_ordered = models.IntegerField(default=20)
