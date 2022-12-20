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
            print("+++++++create")
            return redirect('account_type/show', {'account_type': form})
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
    form = AccountTypeForm(request.POST, instance=account_type)
    if form.is_valid():
        form.save()
        return redirect('account_type/show', {'account_type': form})
    return render(request, 'account_type/edit.html', {'account_type': account_type})


def destroy(request, id):
    account_type = AccountType.objects.get(id=id)
    account_type.delete()
    return redirect("/show")
