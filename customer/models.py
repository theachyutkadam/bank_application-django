from django.db import models
from account_type.models import AccountType


class Customer(models.Model):
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15)
    amount_limit = models.FloatField()
    current_balance = models.FloatField()

    class Meta:
        db_table = "customer"
