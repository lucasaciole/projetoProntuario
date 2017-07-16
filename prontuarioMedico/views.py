from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from prontuarioMedico.data_base import sql_consultas, sql_inserts
from .forms import CuidadorForm
from .forms import NameForm

def home(request):
    nro_pacientes = sql_consultas.get_qtd_pacientes()
    nro_cuidadores = sql_consultas.get_qtd_cuidadores()
    nro_responsabilidades = sql_consultas.get_qtd_responsabilidades()
    qtd_atendimentos_no_ultimo_mes =sql_consultas.get_qtd_atendimento_no_ultimo_mes()
    META_DE_ATENDIMENTOS=8
    frac_meta_atendimento=str(int(100*qtd_atendimentos_no_ultimo_mes/META_DE_ATENDIMENTOS))
    context_dictionary = {'pagina': 'home',
                          'nro_pacientes': nro_pacientes,
                          'nro_cuidadores': nro_cuidadores,
                          'nro_responsabilidades':nro_responsabilidades,
                          'frac_meta_atendimento':frac_meta_atendimento}

    return render(request, 'prontuarioMedico/home.html', context_dictionary)


# Views de paciente
def paciente_index(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #retorna lista de pacientes que possuem 'nome_paciente' contido no seu nome
            pacientes_tuple=sql_consultas.get_pacientes_por_nome(form.cleaned_data['nome_paciente'])
    else:
        pacientes_tuple = sql_consultas.get_paciente()

    pacientes = []
    for paciente_aux in pacientes_tuple:
        pacientes.append({'id_paciente': paciente_aux[0],
                          'nome': paciente_aux[1],
                          'datanascimento': paciente_aux[2]})

    context_dictionary = {'pagina': 'paciente_index',
                         'pacientes': pacientes}
    return render(request, 'prontuarioMedico/paciente/paciente_index.html', context_dictionary)

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Views de Medico
def medico_index(request):
    context_dictionary = {'pagina': 'medico_index'}

    return render(request, 'prontuarioMedico/medico/medico_index.html', context_dictionary)


# Views de cuidador
def cuidador_index(request):
    cuidadores_tuple = sql_consultas.get_cuidador()
    cuidadores = []
    for cuidador_aux in cuidadores_tuple:
        aux = {'cpf': cuidador_aux[0], 'nome': cuidador_aux[1], 'profissional': cuidador_aux[2]}
        cuidadores.append(aux)

    context_dictionary = {'pagina': 'cuidador_index',
                          'cuidadores': cuidadores}

    return render(request, 'prontuarioMedico/cuidador/cuidador_index.html', context_dictionary)


def cuidador_contratos(request):
    print('entrou na contratos')
    return render(request, 'prontuarioMedico/cuidador/cuidador_contratos.html')


def cuidador_novo(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)
        print(form['cpf_cuidador'])
        if form.is_valid():
            sql_inserts.inserir_cuidador(form.cleaned_data)
        else:
            print("invalid")
            return render(request, 'prontuarioMedico/cuidador/cuidador_novo.html', {'form': form})
        return HttpResponseRedirect('/cuidador')
    else:
        form = CuidadorForm()
        return render(request, 'prontuarioMedico/cuidador/cuidador_novo.html', {'form': form})


# Views de Responsavel
def responsavel_responsabilidades(request):
    responsabilidades_tuple = sql_consultas.get_responsabilidade()
    responsabilidades = []
    for responsabilidade in responsabilidades_tuple:
        responsabilidades.append({'id_paciente': responsabilidade[0],
                                  'nome_paciente': responsabilidade[1],
                                  'id_responsavel': responsabilidade[2],
                                  'nome_responsavel': responsabilidade[3],
                                  'grau_parentesco': responsabilidade[4],
                                  'prioridade': responsabilidade[5],
                                  'status': responsabilidade[6]})

    context_dictionary = {'pagina': 'responsabilidades',
                          'responsabilidades': responsabilidades}

    return render(request, 'prontuarioMedico/responsavel/responsabilidades.html', context_dictionary)


# Views de administrador
def admin_index(request):
    context_dictionary = {'pagina': 'admin'}
    return render(request, 'prontuarioMedico/administrador/administrador.html', context_dictionary)
