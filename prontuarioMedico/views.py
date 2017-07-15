from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from prontuarioMedico.data_base import sql_consultas
from .forms import CuidadorForm


def home(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    nro_cuidadore = sql_consultas.get_qtd_cuidadores()
    context_dictionary = {'pagina': 'home',
                          'nro_pacientes': nro_pacientes,
                          'nro_cuidadores': nro_cuidadore}
    return render(request, 'prontuarioMedico/home.html', context_dictionary)

# Views de paciente
def paciente_index(request):
    context_dictionary = {'pagina': 'paciente'}

    return render(request, 'prontuarioMedico/paciente/paciente.html', context_dictionary)

# Views de Medico
def medico_index(request):
    context_dictionary = {'pagina': 'medico'}

    return render(request, 'prontuarioMedico/paciente/paciente.html', context_dictionary)


# Views de cuidador
def cuidador_index(request):
    cuidadores_tuple = sql_consultas.get_cuidador()
    cuidadores = []
    for cuidador_aux in cuidadores_tuple:
        aux = {'cpf': cuidador_aux[0], 'nome': cuidador_aux[1], 'profissional': cuidador_aux[2]}
        cuidadores.append(aux)

    context_dictionary = {'pagina': 'cuidador',
                          'cuidadores': cuidadores}

    return render(request, 'prontuarioMedico/cuidador/cuidador_index.html', context_dictionary)

def cuidador_contratos(request):
    print('entrou na contratos')
    return render(request, 'prontuarioMedico/cuidador/cuidador_contratos.html')

def cuidador_novo(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)
        print(form)
        return HttpResponseRedirect('/cuidador')
    else:
        form = CuidadorForm()
        print(form['nome'])
        return render(request, 'prontuarioMedico/cuidador/cuidador_novo.html', {'form': form})


# Views de Responsavel
def responsavel_index(request):
    context_dictionary = {'pagina': 'responsavel'}

    return render(request, 'prontuarioMedico/responsavel/responsavel.html', context_dictionary)


# Views de administrador
def admin_index(request):
    context_dictionary = {'pagina': 'admin'}

    return render(request, 'prontuarioMedico/administrador/administrador.html', context_dictionary)

