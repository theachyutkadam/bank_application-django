from django.db import models
from customer.models import Customer


class Card(models.Model):
    title = models.CharField(max_length=15)
    number = models.CharField(max_length=15)
    expiry_date = models.DateField()
    cvv_code = models.IntegerField(max_length=3)
    status = models.CharField(max_length=10)
    is_deleted = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "card"
