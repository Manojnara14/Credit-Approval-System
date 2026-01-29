
from django.db import models
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    monthly_income = models.IntegerField()
    approved_limit = models.IntegerField()
