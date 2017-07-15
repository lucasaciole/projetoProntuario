from django.http import HttpResponse
from django.shortcuts import render
from prontuarioMedico import data_base
from prontuarioMedico.data_base import sql_consultas


def home(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    nro_cuidadore = sql_consultas.get_qtd_cuidadores()
    context_dictionary = {'pagina': 'home',
                          'nro_pacientes': nro_pacientes,
                          'nro_cuidadores': nro_cuidadore}
    return render(request, 'prontuarioMedico/home.html', context_dictionary)

# Views de paciente
def paciente(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    return render(request, 'prontuarioMedico/paciente/paciente.html', {'pagina': 'paciente', 'nro_pacientes':nro_pacientes})


# Views de cuidador
def cuidador(request):
    return render(request, 'prontuarioMedico/cuidador/cuidador.html', {})


# Views de administrador
def admin(request):
    return render(request, 'prontuarioMedico/administrador/administrador.html', {})

