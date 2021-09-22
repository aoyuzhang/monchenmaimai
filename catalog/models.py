from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    url = models.CharField(max_length =100)
    industry = models.CharField(max_length = 100)
    director = models.CharField(max_length = 100)
    number_of_employee = models.IntegerField()
    naics = models.IntegerField()
    corporation_id = models.IntegerField()

