from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=32,unique=True)
    department_intake = models.IntegerField()


    def __str__(self):
        return f"{self.id} {self.department_name}"