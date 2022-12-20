from django.shortcuts import render, redirect
from customer.forms import CustomerForm
from customer.models import Customer
# Create your views here.


def index(request):
    customers = Customer.objects.all()
    return render(request, "customer/index.html", {'customers': customers})


def create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            department = Department.objects.last()
            return render(request, 'customer/show.html', {'customer': department})
    else:
        form = CustomerForm()
    return render(request, 'customer/new.html')


def show(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "customer/show.html", {'customer': customer})


def new(request):
    return render(request, "customer/new.html")


def edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customer/edit.html', {'customer': customer})


def update(request, id):
    customer = Customer.objects.get(id=id)
    customer.name = request.POST['name']
    customer.loan_intrest_rate = request.POST['loan_intrest_rate']
    customer.saving_intrest_rate = request.POST['saving_intrest_rate']
    customer.save()
    return render(request, "customer/show.html", {'customer': customer})


def destroy(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customer")
