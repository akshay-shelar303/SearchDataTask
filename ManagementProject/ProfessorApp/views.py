from django.shortcuts import render,redirect
from .models import Professor
from .forms import ProfessorForm


def add_professor(request):
    form = ProfessorForm()
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_professor")
    template_name = "ProfessorApp/professor.html"
    context = {'form':form}
    return render(request, template_name, context)

def showprofessor(request):
    professor_list = Professor.objects.all()
    if request.method == 'POST':
        professor_list = Professor.objects.filter(professor_name__icontains=request.POST['searchdata'])
    template_name = "ProfessorApp/show_professor.html"
    context = {'professor_list':professor_list}
    return render(request, template_name, context)

def update_professor(request,i):
    professor = Professor.objects.get(id=i)
    form = ProfessorForm(instance=professor)
    if request.method == 'POST':
        form = ProfessorForm(request.POST,instance=professor)
        if form.is_valid():
            form.save()
            return redirect("show_professor")
    template_name = "ProfessorApp/professor.html"
    context = {'form':form}
    return render(request, template_name, context)


def delete_professor(request,i):
    professor = Professor.objects.get(id=i)
    professor.delete()
    return redirect("show_professor")


