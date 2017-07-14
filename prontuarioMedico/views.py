from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Home")


def home(request):
    return render(request, 'prontuarioMedico/home.html', {})
