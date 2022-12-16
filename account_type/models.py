from django.db import models
class AccountType(models.Model):
    name = models.CharField(max_length=25)
    loan_intrest_rate = models.FloatField()
    saving_intrest_rate = models.FloatField()
    class Meta:
        db_table = "account_type"
