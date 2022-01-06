import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ManagementProject.settings')
django.setup()

from faker import Faker
import random
from StudentApp.models import Student
from DepartmentApp.models import Department
from ProfessorApp.models import Professor


dept_list = list(Department.objects.all())
fake = Faker()
#
# def generateStudentData(n):
#     for i in range(n):
#         student_name = fake.name()
#         student_marks = random.randint(10,100)
#         department = random.choice(dept_list)
#         department = fake.random_element(dept_list)
#         student_obj = Student.objects.create(student_name=student_name,student_marks=student_marks,department=department)
#
# generateStudentData(2)

def generateProfessorData(n):
    for i in range(n):
        professor_name = fake.name()
        salary = random.randint(5,100)
        l = random.randint(2,4)
        department = fake.random_elements(dept_list,length=l,unique=True)
        professor_obj = Professor.objects.create(professor_name=professor_name,salary=salary)
        professor_obj.department.set(department)

generateProfessorData(2)