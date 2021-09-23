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


class Topic(models.Model):
    # other fields...
    # Add `auto_now_add=True` to the `last_updated` field
    last_updated = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    # other fields...
    # Add `null=True` to the `updated_by` field
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete = models.CASCADE)