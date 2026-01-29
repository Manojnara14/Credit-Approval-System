
from django.db import models
from customers.models import Customer

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    tenure = models.IntegerField()
    monthly_installment = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
