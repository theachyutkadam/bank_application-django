from django.shortcuts import render, HttpResponseRedirect
from .models import Address
from .forms import AddressForm
# Create your views here.

# This Function will Add new Item and Show all items
def add_show(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            bl = form.cleaned_data['building']
            fn = form.cleaned_data['flat_number']
            ds = form.cleaned_data['district']
            st = form.cleaned_data['state']
            # pn = form.cleaned_data['pincode']
            reg = Address(name=nm, building=bl, flat_number=fn, district=ds, state=st,)
            reg.save()
        form = AddressForm()
    else:
        form = AddressForm()
    # stud = User.objects.all()
    return render(request, 'address/show.html', {'form':form, 'address':Address.objects.all()})

# This Function will Delete

def delete_data(request, id):
    if request.method == 'POST':
        pi = Address.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/address')

#This Function will updateor edir

def update_data(request, id):
    if request.method == 'POST':
        pi = Address.objects.get(pk=id)
        fm = AddressForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            form = AddressForm()
            return render(request, 'address/show.html', {'form':form, 'address':Address.objects.all()})
    else:
        pi = Address.objects.get(pk=id)
        fm = AddressForm(instance=pi)
    return render(request, 'address/edit.html', {'form':fm})

















# from django.shortcuts import render, redirect
# from address.forms import AddressForm
# from address.models import Address
# # Create your views here.
# def index(request):
#     addresses = Address.objects.all()
#     return render(request, "address/show.html", {'addresses': addresses})


# def create(request):
#     if request.method == "POST":
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/show')
#     else:
#         form = AddressForm()
#     return render(request, 'index.html', {'form': form})


# def show(request):
#     address = Address.objects.get(id=id)
#     return render(request, "show.html", {'address': address})

# def edit(request, id):
#   address = Address.objects.get(id=id)
#   return render(request,'edit.html', {'address':address})

# def update(request, id):
#   address = Address.objects.get(id=id)
#   form = AddressForm(request.POST, instance = address)
#   if form.is_valid():
#     form.save()
#     return redirect("/show")
#   return render(request, 'edit.html', {'address': address})

# def destroy(request, id):
#   address = Address.objects.get(id=id)
#   address.delete()
#   return redirect("/show")
