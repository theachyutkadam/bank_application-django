from django.db import models
# from manager.models import Manager
from customer.models import Customer
from department.models import Department


class Employee(models.Model):
    salary_amount = models.FloatField()
    date_of_joining = models.DateField()
    work_status = models.CharField(max_length=25)
    designation = models.CharField(max_length=25)
    official_email = models.CharField(max_length=50)
    education = models.CharField(max_length=25)

    # manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee"
