from django.shortcuts import render, redirect
# from user_information.forms import UserInformationForm
# from user_information.models import UserInformation
# Create your views here.
import requests


def index(request):
    response = requests.get('http://localhost:3000/user_informations')
    user_informations = response.json()
    return render(request, "user_information/index.html", {'user_informations': user_informations})
