from django.shortcuts import render, redirect
from .models import Manager
from .forms import ManagerForm

# Create your views here.
def index(request):
    managers = Manager.objects.all()
    return render(request, "manager/index.html", {'managers': managers})

def create(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            manager = Manager.objects.last()
            return render(request, "manager/show.html", {'manager': manager})
    else:
        form = ManagerForm()
    return render(request, 'manager/new.html')


def show(request, id):
    manager = Manager.objects.get(id=id)
    return render(request, "manager/show.html", {'manager': manager})


def new(request):
    return render(request, "manager/new.html")


def edit(request, id):
    manager = Manager.objects.get(id=id)
    return render(request, 'manager/edit.html', {'manager': manager})


def update(request, id):
    manager = Manager.objects.get(id=id)
    manager.name = request.POST['name']
    manager.user_id = request.POST['userid']
    manager.department_id = request.POST['departmentid']
    manager.designation = request.POST['designation']
    manager.save()
    return render(request, "manager/show.html", {'manager': manager})


def destroy(request, id):
    account_type = Manager.objects.get(id=id)
    account_type.delete()
    return redirect("/manager")