from django.db import models
class Address(models.Model):
    name = models.CharField(max_length=25)
    building = models.CharField(max_length=30)
    flat_number = models.CharField(max_length=30)
    road = models.CharField(max_length=150)
    taluka = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=30)

    class Meta:
        db_table = "address"
