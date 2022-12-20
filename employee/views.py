from django.shortcuts import render, redirect
# from employee.forms import EmployeeForm
# from employee.models import Employee
# Create your views here.
import requests


def index(request):
    response = requests.get('http://localhost:3000/employees')
    employees = response.json()
    return render(request, "employee/index.html", {'employees': employees})
