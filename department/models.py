from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=25)
    employee_count = models.IntegerField((""))

    class Meta:
        db_table = "department"