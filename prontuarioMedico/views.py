from django.http import HttpResponse
from django.shortcuts import render
from prontuarioMedico.data_base import sql_consultas


def home(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    return render(request, 'prontuarioMedico/home.html', {'pagina':'home','nro_pacientes':nro_pacientes})

def paciente(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    return render(request, 'prontuarioMedico/paciente.html', {'pagina':'paciente','nro_pacientes':nro_pacientes})

def cuidador_index(request):
    cuidadores_tuple = sql_consultas.get_cuidador()
    cuidadores = []
    for cuidador_aux in cuidadores_tuple:
        aux = {'cpf': cuidador_aux[0], 'nome': cuidador_aux[1], 'profissional': cuidador_aux[2]}
        cuidadores.append(aux)

    return render(request, 'prontuarioMedico/cuidador/cuidador_index.html', {'cuidadores': cuidadores})

def cuidador_contratos(request):
    return render(request, 'prontuarioMedico/cuidador/cuidador.html')