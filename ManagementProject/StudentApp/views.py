from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm


def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_student")
    template_name = "StudentApp/student.html"
    context = {'form':form}
    return render(request, template_name, context)

def showstudent(request):
    student_list = Student.objects.all()
    if request.method == 'POST':
        student_list = Student.objects.filter(student_name__icontains=request.POST['searchdata'])
    template_name = "StudentApp/show_student.html"
    context = {'student_list':student_list}
    return render(request, template_name, context)

def update_student(request,i):
    student = Student.objects.get(id=i)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("show_student")
    template_name = "StudentApp/student.html"
    context = {'form':form}
    return render(request, template_name, context)


def delete_student(request,i):
    student = Student.objects.get(id=i)
    student.delete()
    return redirect("show_student")



