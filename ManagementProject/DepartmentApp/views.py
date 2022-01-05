from django.shortcuts import render,redirect
from .models import Department
from .forms import DepartmentForm


def add_departmet(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_department")
    template_name = "DepartmentApp/department.html"
    context = {'form':form}
    return render(request, template_name, context)

def showdepartment(request):
    department_list = Department.objects.all()
    if request.method == 'POST':
        department = Department.objects.filter(department_name__icontains=request.POST['searchdata'])
        professor = department[0].department_pro.all()
        student = department[0].department_stu.all()
        template_name = "DepartmentApp/searchdept.html"
        context = {'department':department,'professor':professor,'student':student}
        return render(request, template_name, context)
    template_name = "DepartmentApp/show_dept.html"
    context = {'department_list':department_list}
    return render(request, template_name, context)

def update_departmet(request,i):
    department = Department.objects.get(id=i)
    form = DepartmentForm(instance=department)
    if request.method == 'POST':
        form = DepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return redirect("show_department")
    template_name = "DepartmentApp/department.html"
    context = {'form':form}
    return render(request, template_name, context)


def delete_department(request,i):
    department = Department.objects.get(id=i)
    department.delete()
    return redirect("show_department")

