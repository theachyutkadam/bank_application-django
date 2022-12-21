from django.shortcuts import render, redirect
from card.forms import CardForm
from card.models import Card
from customer.models import Customer
# Create your views here.


def index(request):
    cards = Card.objects.all()
    return render(request, "card/index.html", {'cards': cards})


def create(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            card = Card.objects.last()
            return render(request, 'card/show.html', {'card': card})
    else:
        form = CardForm()
    return render(request, 'card/new.html')


def show(request, id):
    card = Card.objects.get(id=id)
    customers = Customer.objects.all()
    return render(request, "card/show.html", {'card': card, 'customers': customers})


def new(request):
    customers = Customer.objects.all()
    return render(request, "card/new.html", {'customers': customers})


def edit(request, id):
    card = Card.objects.get(id=id)
    return render(request, 'card/edit.html', {'card': card})


def update(request, id):
    card = Card.objects.get(id=id)
    card.title = request.POST['title']
    card.number = request.POST['number']
    card.expiry_date = request.POST['expiry_date']
    card.cvv_code = request.POST['cvv_code']
    card.status = request.POST['status']
    card.is_deleted = request.POST['is_deleted']
    # card.customer = request.POST['customer']
    card.save()
    return render(request, "card/show.html", {'card': card})


def destroy(request, id):
    card = Card.objects.get(id=id)
    card.delete()
    return redirect("/card")
