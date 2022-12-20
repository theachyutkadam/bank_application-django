from django.shortcuts import render, redirect
from account_type.forms import AccountTypeForm
from account_type.models import AccountType
# Create your views here.


def index(request):
    account_types = AccountType.objects.all()
    return render(request, "account_type/index.html", {'account_types': account_types})


def create(request):
    if request.method == "POST":
        form = AccountTypeForm(request.POST)
        if form.is_valid():
            form.save()
            department = Department.objects.last()
            return render(request, 'account_type/show.html', {'account_type': department})
    else:
        form = AccountTypeForm()
    return render(request, 'account_type/new.html')


def show(request, id):
    account_type = AccountType.objects.get(id=id)
    return render(request, "account_type/show.html", {'account_type': account_type})


def new(request):
    return render(request, "account_type/new.html")


def edit(request, id):
    account_type = AccountType.objects.get(id=id)
    return render(request, 'account_type/edit.html', {'account_type': account_type})


def update(request, id):
    account_type = AccountType.objects.get(id=id)
    account_type.name = request.POST['name']
    account_type.loan_intrest_rate = request.POST['loan_intrest_rate']
    account_type.saving_intrest_rate = request.POST['saving_intrest_rate']
    account_type.save()
    return render(request, "account_type/show.html", {'account_type': account_type})


def destroy(request, id):
    account_type = AccountType.objects.get(id=id)
    account_type.delete()
    return redirect("/account_type")
