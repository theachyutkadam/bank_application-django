from django.shortcuts import render, redirect
# from user.forms import UserForm
# from user.models import User
# from user.models import User
# Create your views here.
import requests


def index(request):
    # response = requests.get('http://localhost:3000/users')
    # users = response.json()
    # users = User.objects.all()
    return render(request, "user/index.html", {'users': users})
