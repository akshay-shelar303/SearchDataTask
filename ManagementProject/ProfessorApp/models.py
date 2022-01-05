from django.db import models
from DepartmentApp.models import Department

class Professor(models.Model):
    department = models.ManyToManyField(Department,related_name='department_pro')
    professor_name = models.CharField(max_length=32)
    salary = models.IntegerField()

    def __str__(self):
        return self.professor_name
