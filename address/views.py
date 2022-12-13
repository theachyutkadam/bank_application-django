from django.shortcuts import render, redirect
from address.forms import AddressForm
from address.models import Address
# Create your views here.
def index(request):
    addresses = Address.objects.all()
    return render(request, "show.html", {'addresses': addresses})


def create(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = AddressForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    address = Address.objects.get(id=id)
    return render(request, "show.html", {'address': address})

def edit(request, id):
  address = Address.objects.get(id=id)
  return render(request,'edit.html', {'address':address})

def update(request, id):
  address = Address.objects.get(id=id)
  form = AddressForm(request.POST, instance = address)
  if form.is_valid():
    form.save()
    return redirect("/show")
  return render(request, 'edit.html', {'address': address})

def destroy(request, id):
  address = Address.objects.get(id=id)
  address.delete()
  return redirect("/show")
