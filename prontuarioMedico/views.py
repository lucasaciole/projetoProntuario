from django.http import HttpResponseRedirect
from django.shortcuts import render

from prontuarioMedico.data_base import sql_consultas, sql_inserts
from .forms import CuidadorForm, AtendimentoForm, intercorrenciaForm, atividadeForm, medidaForm
from .forms import NameForm
from .forms import ContratoForm


def home(request):
    META_DE_ATENDIMENTOS = 8  # Meta de atendimentos dentro do periodo de um mês

    valores_home = sql_consultas.get_valores_home()
    nro_pacientes = valores_home[0]
    nro_medicos = valores_home[1]
    nro_cuidadores = valores_home[2]
    nro_responsabilidades = valores_home[3]
    qtd_atendimentos_no_ultimo_mes = sql_consultas.get_qtd_atendimento_no_ultimo_mes()
    frac_meta_atendimento = str(int(100 * qtd_atendimentos_no_ultimo_mes / META_DE_ATENDIMENTOS))

    context_dictionary = {'pagina': 'home',
                          'nro_pacientes': nro_pacientes,
                          'nro_cuidadores': nro_cuidadores,
                          'nro_medicos': nro_medicos,
                          'nro_responsabilidades': nro_responsabilidades,
                          'frac_meta_atendimento': frac_meta_atendimento}

    return render(request, 'prontuarioMedico/home.html', context_dictionary)


# Views de paciente
def paciente_index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # retorna lista de pacientes que possuem 'nome_paciente' contido no seu nome
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
    medicos_tupla = sql_consultas.get_medicos()

    medicos = []
    for medico in medicos_tupla:
        medicos .append({'crm': medico[0],
                          'nome': medico[1],
                          'cidade': medico[2],
                          'especialidade': medico[3]})

    context_dictionary = {'pagina': 'medico_index',
                          'medicos': medicos}
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
               'cpf_paciente': contrato_aux[4],
               'nome_paciente': contrato_aux[5],
               'data_inicio': contrato_aux[6],
               'data_fim': contrato_aux[7],
               'tipo_atendimento': contrato_aux[8],
               'dia_vencimento': contrato_aux[9],
               'valor_atendimento': contrato_aux[10],
               'periodicidade': contrato_aux[11]
               })
    context_dictionary = {'pagina': 'cuidador_contratos',
                          'contratos': contratos}
    return render(request, 'prontuarioMedico/cuidador/cuidador_contratos.html', context_dictionary)

def cuidador_contrato_detalhes(request, id):
    contrato_aux = sql_consultas.get_contratos_por_id(id)
    contrato = {
        'cpf_cuidador': contrato_aux[0][1],
        'nome_cuidador': contrato_aux[0][2],
        'tipo_cuidador':contrato_aux[0][3],
        'cpf_paciente': contrato_aux[0][4],
        'nome_paciente': contrato_aux[0][5],
        'data_inicio': contrato_aux[0][6],
        'data_fim': contrato_aux[0][7],
        'tipo_atendimento': contrato_aux[0][8],
        'dia_vencimento': contrato_aux[0][9],
        'valor_atendimento': contrato_aux[0][10],
        'periodicidade': contrato_aux[0][11]
    }
    profissional = {}
    if contrato['tipo_cuidador'] == 'p':
        profissional_tuple = sql_consultas.get_cuidadorprofissional(contrato['cpf_cuidador'])
        profissional = {
            'entidadedeclasse': profissional_tuple[0][1],
            'numeroentidadedeclasse': profissional_tuple[0][2]
        }

    return render(request, 'prontuarioMedico/cuidador/cuidador_contratos_detalhes.html', {'pagina': 'cuidador_contratos', 'form': contrato, 'profissional': profissional})


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
    profissional = {}
    if (cuidador['tipoCuidador'] == 'p'):
        profissional_tuple = sql_consultas.get_cuidadorprofissional(cuidador['cpf_cuidador'])
        profissional = {
            'entidadedeclasse': profissional_tuple[0][1],
            'numeroentidadedeclasse': profissional_tuple[0][2]
        }
    return render(request, 'prontuarioMedico/cuidador/cuidador_detalhes.html',
                  {'pagina': 'cuidador_detalhes', 'form': cuidador, 'telefone': telefones})


def cuidador_contrato_novo(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            ret = sql_inserts.inserir_contrato(form.cleaned_data)
            print(ret)
        else:
            return render(request, 'prontuarioMedico/cuidador/cuidador_contratos_novo.html', {'pagina': 'cuidador_contratos', 'form': form})
        return HttpResponseRedirect('/cuidador/contratos/')
    else:
        form = ContratoForm()
        return render(request, 'prontuarioMedico/cuidador/cuidador_contratos_novo.html', {'pagina': 'cuidador_contratos' ,'form': form})


def cuidador_atendimentos(request):
    atendimentos_tuple = sql_consultas.get_atendimentos()
    atendimentos = []
    for atendimento in atendimentos_tuple:
        atendimentos.append({'id': atendimento[0],
                             'horario_inicio': atendimento[1],
                             'horario_fim': atendimento[2],
                             'cpf_cuidador': atendimento[3],
                             'nome_cuidador': atendimento[4],
                             'cpf_paciente': atendimento[5],
                             'nome_paciente': atendimento[6]})

    context_dictionary = {'pagina': 'cuidador_atendimentos',
                          'atendimentos': atendimentos}
    return render(request, 'prontuarioMedico/cuidador/cuidador_atendimentos.html', context_dictionary)


def cuidador_atendimentos_detalhes(request, id):
    atendimento_tuple = sql_consultas.get_atendimento_por_id(id)
    print(atendimento_tuple)
    atendimento = {'id': atendimento_tuple['atendimento'][0],
                   'horario_inicio': atendimento_tuple['atendimento'][1],
                   'horario_fim': atendimento_tuple['atendimento'][2],
                   'cpf_cuidador': atendimento_tuple['atendimento'][3],
                   'nome_cuidador': atendimento_tuple['atendimento'][4],
                   'cpf_paciente': atendimento_tuple['atendimento'][5],
                   'nome_paciente': atendimento_tuple['atendimento'][6],
                   }

    intercorrencias = []
    for intercorrencia in atendimento_tuple['intercorrencias']:
        intercorrencias.append(intercorrencia[0])
        print(intercorrencia[0])

    atividades = []
    for atividade in atendimento_tuple['atividades']:
        medidas = []
        for medida in sql_consultas.get_medidas_atividade(atividade[0]):
            medidas.append({'id': medida[0],
                            'nome': medida[2],
                            'aparelho': medida[3],
                            'valor': medida[4],
                            'unidade': medida[5]})

        atividades.append({'id': atividade[0],
                           'nome_atividade': atividade[2],
                           'medidas': medidas})

    context_dictionary = {'pagina': 'cuidador_atendimentos_detalhes',
                          'atendimento': atendimento,
                          'intercorrencias': intercorrencias,
                          'atividades': atividades}

    return render(request, 'prontuarioMedico/cuidador/cuidador_atendimentos_detalhes.html', context_dictionary)


def novo_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            id_novo_atendimento = sql_inserts.inserir_atendimento(form.cleaned_data)
        else:
            print("invalid")
            return render(request, 'prontuarioMedico/cuidador/novo_atendimento.html', {'form': form})
        return HttpResponseRedirect('/cuidador/atendimento/' + str(1))
    else:
        form = AtendimentoForm()
        return render(request, 'prontuarioMedico/cuidador/novo_atendimento.html', {'form': form})


def atendimento_nova_intercorrencia(request, id):
    if request.method == 'POST':
        form = intercorrenciaForm(request.POST)
        if form.is_valid():
            status = sql_inserts.inserir_intercorrencia(form.cleaned_data, id)
            print(status)

        return HttpResponseRedirect('/cuidador/atendimento/' + str(id))
    else:
        form = intercorrenciaForm()
        context_dictionary = {'atendimento': id,
                              'form': form}
        return render(request, 'prontuarioMedico/cuidador/atendimento_nova_intercorrencia.html', context_dictionary)


def atendimento_nova_atividade(request, id):
    if request.method == 'POST':
        form = atividadeForm(request.POST)
        if form.is_valid():
            id_atividade = sql_inserts.inserir_atividade(form.cleaned_data, id)
            print(id_atividade)

        return HttpResponseRedirect('/cuidador/atendimento/' + str(id) + '/atividade/' + str(id_atividade) + '/nova_medida/')
    else:
        form = atividadeForm()
        context_dictionary = {'atendimento': id,
                              'form': form}
        return render(request, 'prontuarioMedico/cuidador/atendimento_nova_atividade.html', context_dictionary)


def atendimento_nova_medida(request, id_atendimento, id_atividade):
    if request.method == 'POST':
        form = medidaForm(request.POST)
        if form.is_valid():
            sql_inserts.inserir_medida(form.cleaned_data, id_atividade)

        if 'finalizar' in request.POST:
            return HttpResponseRedirect('/cuidador/atendimento/' + str(id_atendimento))
        else:
            print('add')

            return HttpResponseRedirect(
                '/cuidador/atendimento/' + str(id_atendimento) + '/atividade/' + str(id_atividade) + '/nova_medida/')


    else:
        form = medidaForm()
        context_dictionary = {'atendimento': id_atendimento,
                              'atividade':id_atividade,
                              'form': form}
        return render(request, 'prontuarioMedico/cuidador/atividade_nova_medida.html', context_dictionary)


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


def cuidador_planos(request):
    pass

# Views de administrador
def admin_index(request):
    context_dictionary = {'pagina': 'admin'}
    return render(request, 'prontuarioMedico/administrador/administrador.html', context_dictionary)
