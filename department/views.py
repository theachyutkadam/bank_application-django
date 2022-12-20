from django.shortcuts import render, redirect
from .forms import DepartmentForm
from .models import Department
# Create your views here.


def index(request):
    departments = Department.objects.all()
    return render(request, "department/index.html", {'departments': departments})


def create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            department = Department.objects.last()
            return render(request, "department/show.html", {'department': department})
    else:
        form = DepartmentForm()
    return render(request, 'department/new.html')


def show(request, id):
    department = Department.objects.get(id=id)
    return render(request, "department/show.html", {'department': department})


def new(request):
    return render(request, "department/new.html")


def edit(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'department/edit.html', {'department': department})


def update(request, id):
    department = Department.objects.get(id=id)
    department.name = request.POST['name']
    department.employee_count = request.POST['employees']
    department.save()
    return render(request, "department/show.html", {'department': department})


def destroy(request, id):
    account_type = Department.objects.get(id=id)
    account_type.delete()
    return redirect("/department")
