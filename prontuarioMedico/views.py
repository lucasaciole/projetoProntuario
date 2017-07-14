from django.http import HttpResponse
from django.shortcuts import render
from prontuarioMedico import data_base
from prontuarioMedico.data_base import sql_consultas


def home(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    return render(request, 'prontuarioMedico/home.html', {'pagina':'home','nro_pacientes':nro_pacientes})

def paciente(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    return render(request, 'prontuarioMedico/paciente.html', {'pagina':'paciente','nro_pacientes':nro_pacientes})
