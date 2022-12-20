from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=25)
    user_id = models.IntegerField()
    department_id = models.IntegerField()
    designation = models.CharField(max_length=20)
    
    class Meta:
        db_table = "manager"