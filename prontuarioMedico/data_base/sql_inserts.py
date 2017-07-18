from django.db import connection


def inserir_cuidador(form):
    cursor = connection.cursor()
    insert = "insert into v_detalhes_cuidador(cpf_cuidador, nome, tipocuidador, datanascimento, logradouro, numero, complemento, bairro, cidade, estado, cep, rg)"
    insert += "values (%s, %s, %s, to_date(%s, 'yyyy-mm-dd'), %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert, (
    form['cpf_cuidador'], form['nome'], form['tipoCuidador'], form['datanascimento'], form['logradouro'],
    form['numero'], form['complemento'], form['bairro'], form['cidade'], form['estado'], form['cep'], form['rg']))
    return cursor.statusmessage


def inserir_contrato(form):
    cursor = connection.cursor()
    print(form)
    insert_str = "insert into contrato(cpf_paciente, cpf_cuidador, datainicio, datafim, tipoatendimento, diavencimento, valoratendimento, periodicidade) "
    insert_str += "values (%s, %s, to_date(%s, 'dd/mm/yyyy'), to_date(%s, 'dd/mm/yyyy'), %s, %s, %s, %s)"
    cursor.execute(insert_str, (
    form['cpf_paciente'], form['cpf_cuidador'], form['datainicio'], form['datafim'], form['tipoatendimento'],
    form['diavencimento'], form['valoratendimento'], form['periodicidade']))
    return cursor.statusmessage


def inserir_planoatendimento(form):
    cursor = connection.cursor()
    insert_str = "insert into planoatendimento(fk_id_contrato, dataplano, nomeplano) "
    insert_str += "values (%s, to_timestamp(%s, 'dd/mm/yyyy HH24hmi'), %s)"
    cursor.execute(insert_str, (form['id_contrato'], form['dataplano'], form['nomeplano']))
    return cursor.statusmessage


def inserir_atividadeprevista(form):
    cursor = connection.cursor()
    insert_str = "insert into atividadeprevista(fk_id_planoatendimento, tipo, descricao) "
    insert_str += "values (%s, %s, %s)"
    cursor.execute(insert_str, (form['id_plano'], form['tipo'], form['descricao']))
    return cursor.statusmessage


def inserir_atendimento(form):
    cursor = connection.cursor()
    cursor.execute("SELECT inserir_atendimento_plano_recente(%s, %s, %s, %s, TRUE, NULL)",
                   (form['horario_inicial'], form['horario_final'], form['cpf_cuidador'], form['cpf_paciente']))

    id_atividade = cursor.fetchall()
    return id_atividade[0][0]

def inserir_intercorrencia(form, id):
    cursor = connection.cursor()

    insert = "INSERT INTO intercorrenciaatendimentocuidador(id_atendimentocuidador, intercorrencia) values (%s, %s)"
    cursor.execute(insert, (id, form['intercorrencia']))

    return cursor.statusmessage


def inserir_atividade(form, id):
    cursor = connection.cursor()
    print(form['nome'])

    cursor.execute("SELECT inserir_atividade(%s,%s)", (id, form['nome']))

    id_atividade = cursor.fetchall()

    return id_atividade[0][0]


def inserir_medida(form, id):
    cursor = connection.cursor()

    insert = "insert into medidaatividade(fk_atividade, nomemedida, aparelhomedida, valormedida, unidademedida)"
    insert += "values (%s, %s, %s, %s, %s)"

    cursor.execute(insert, (id, form['medida'], form['aparelho'], form['valor'], form['unidade']))
