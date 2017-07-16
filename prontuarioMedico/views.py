from django.http import HttpResponseRedirect
from django.shortcuts import render
from prontuarioMedico.data_base import sql_consultas, sql_inserts
from .forms import CuidadorForm
from .forms import NameForm

def home(request):
    META_DE_ATENDIMENTOS = 8 # Meta de atendimentos dentro do periodo de um mês

    valores_home = sql_consultas.get_valores_home()
    nro_pacientes = valores_home[0]
    nro_cuidadores = valores_home[1]
    nro_responsabilidades = valores_home[2]
    qtd_atendimentos_no_ultimo_mes = sql_consultas.get_qtd_atendimento_no_ultimo_mes()
    frac_meta_atendimento = str(int(100 * qtd_atendimentos_no_ultimo_mes / META_DE_ATENDIMENTOS))

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
            pacientes_tuple = sql_consultas.get_pacientes_por_nome(form.cleaned_data['nome_paciente'])
        else:
            pacientes_tuple = sql_consultas.get_paciente()
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
    contratos_tuple = sql_consultas.get_contratos()
    contratos = []
    for contrato_aux in contratos_tuple:
        contratos.append({'id_contrato': contrato_aux[0],
               'cpf_cuidador': contrato_aux[1],
               'nome_cuidador': contrato_aux[2],
               'cpf_paciente': contrato_aux[3],
               'nome_paciente': contrato_aux[4],
               'data_inicio': contrato_aux[5],
               'data_fim': contrato_aux[6],
               'tipo_atendimento': contrato_aux[7],
               'dia_vencimento': contrato_aux[8],
               'valor_atendimento': contrato_aux[9],
               'periodicidade': contrato_aux[10]
               })
    context_dictionary = {'pagina': 'contratos',
                          'contratos': contratos}
    return render(request, 'prontuarioMedico/cuidador/cuidador_contratos.html', context_dictionary)


def cuidador_novo(request):
    if request.method == 'POST':
        form = CuidadorForm(request.POST)
        print(form['cpf_cuidador'])
        if form.is_valid():
            ret = sql_inserts.inserir_cuidador(form.cleaned_data)
            print(ret)
        else:
            print("invalid")
            return render(request, 'prontuarioMedico/cuidador/cuidador_novo.html', {'form': form})
        return HttpResponseRedirect('/cuidadores')
    else:
        form = CuidadorForm()
        return render(request, 'prontuarioMedico/cuidador/cuidador_novo.html', {'form': form})

def cuidador_detalhes(request, id):
    cuidador_tuple = sql_consultas.get_cuidador_por_cpf(id)
    cuidador = {
        'cpf_cuidador': cuidador_tuple[0][0],
        'nome': cuidador_tuple[0][1],
        'tipoCuidador': cuidador_tuple[0][2],
        'datanascimento': cuidador_tuple[0][3],
        'logradouro': cuidador_tuple[0][4],
        'numero': cuidador_tuple[0][5],
        'complemento': cuidador_tuple[0][6],
        'bairro': cuidador_tuple[0][7],
        'cidade': cuidador_tuple[0][8],
        'estado': cuidador_tuple[0][9],
        'cep': cuidador_tuple[0][10],
        'rg': cuidador_tuple[0][11],
    }
    telefone_tuple = sql_consultas.get_telefone_cuidador(id)
    telefones = []
    for aux in telefone_tuple:
        telefones.append({'tipo': aux[0],
                          'telefone': aux[1] })
    return render(request, 'prontuarioMedico/cuidador/cuidador_detalhes.html', {'pagina': 'cuidador_detalhes', 'form': cuidador, 'telefone': telefones})


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
