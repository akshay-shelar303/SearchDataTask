from django.db import models
from DepartmentApp.models import Department

class Student(models.Model):
    department = models.ForeignKey(Department,related_name='department_stu',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=32)
    student_marks = models.FloatField()

    def __str__(self):
        return self.student_name
