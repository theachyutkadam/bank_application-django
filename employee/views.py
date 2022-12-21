

from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from department.models import Department
from customer.models import Customer
# Create your views here.

# import requests
# def index(request):
#     response = requests.get('http://localhost:3000/employees')
#     employees = response.json()
#     return render(request, "employee/index.html", {'employees': employees})


def index(request):
    employees = Employee.objects.all()
    return render(request, "employee/index.html", {'employees': employees})


def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            employee = Employee.objects.last()
            return render(request, 'employee/show.html', {'employee': employee})
    else:
        form = EmployeeForm()
    return render(request, 'employee/new.html')


def show(request, id):
    employee = Employee.objects.get(id=id)
    departments = Department.objects.all()
    customers = Customer.objects.all()
    # managers = Manager.objects.all()
    return render(request, "employee/show.html", {'employee': employee, 'customers': customers, 'departments': departments})


def new(request):
    customers = Customer.objects.all()
    departments = Department.objects.all()
    # managers = Manager.objects.all()
    return render(request, "employee/new.html", {'customers': customers, 'departments': departments})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    customers = Customer.objects.all()
    departments = Department.objects.all()
    return render(request, 'employee/edit.html', {'employee': employee, 'customers': customers, 'departments': departments})


def update(request, id):
    employee = Employee.objects.get(id=id)
    employee.salary_amount = request.POST['salary_amount']
    employee.date_of_joining = request.POST['date_of_joining']
    employee.work_status = request.POST['work_status']
    employee.designation = request.POST['designation']
    employee.official_email = request.POST['official_email']
    employee.education = request.POST['education']
    # employee.manager = request.POST['manager']
    # employee.customer = request.POST['customer']
    # employee.department = request.POST['department']
    employee.save()
    return render(request, "employee/show.html", {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/employee")
