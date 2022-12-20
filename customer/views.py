from django.shortcuts import render, redirect
from customer.forms import CustomerForm
from customer.models import Customer
from account_type.models import AccountType
# Create your views here.


def index(request):
    customers = Customer.objects.all()
    return render(request, "customer/index.html", {'customers': customers})


def create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            customer = Customer.objects.last()
            return render(request, 'customer/show.html', {'customer': customer})
    else:
        form = CustomerForm()
    return render(request, 'customer/new.html')


def show(request, id):
    customer = Customer.objects.get(id=id)
    account_types = AccountType.objects.all()
    return render(request, "customer/show.html", {'customer': customer}, {'account_types': account_types})


def new(request):
    account_types = AccountType.objects.all()
    return render(request, "customer/new.html", {'account_types': account_types})


def edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customer/edit.html', {'customer': customer})


def update(request, id):
    customer = Customer.objects.get(id=id)
    customer.amount_limit = request.POST['amount_limit']
    customer.current_balance = request.POST['current_balance']
    customer.account_number = request.POST['account_number']
    # customer.account_type = request.POST['account_type']
    customer.save()
    return render(request, "customer/show.html", {'customer': customer})


def destroy(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/customer")
