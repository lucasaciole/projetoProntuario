from django.http import HttpResponse
from django.shortcuts import render
from prontuarioMedico import DataBase
from prontuarioMedico.DataBase import operacoesSql


def home(request):
    operacoesSql.teste()
    return render(request, 'prontuarioMedico/home.html', {})
