from django.db import connection


# Consultas de quantidades
def get_valores_home():
    cursor = connection.cursor()
    cursor.execute("SELECT dados_para_home()")
    row = cursor.fetchall()
    return row[0][0]


# Consultas de tabelas
def get_cuidador():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_CUIDADOR ORDER BY TIPO DESC, NOME")
    row = cursor.fetchall()
    return row

def get_cuidadorprofissional(cpf):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cuidadorprofissional WHERE cpf_cuidador = %s", (cpf,))
    row = cursor.fetchall()
    return row


def get_cuidador_por_cpf(cpf):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_DETALHES_CUIDADOR WHERE cpf_cuidador = %s", (cpf,))
    row = cursor.fetchall()
    return row


def get_telefone_cuidador(cpf):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_TELEFONES_CUIDADORES WHERE cpf_cuidador= %s", (cpf,))
    row = cursor.fetchall()
    return row


def get_paciente():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTE")
    row = cursor.fetchall()
    return row


# Retorna todos pacientes que possuem 'nome' como substring (case insensitive)
def get_pacientes_por_nome(nome):

    cursor = connection.cursor()
    sqlquery ="SELECT * FROM PACIENTE WHERE LOWER(nome) LIKE LOWER(%s);"
    params = "%"+str(nome)+"%"
    cursor.execute(sqlquery, (params,))
    row = cursor.fetchall()
    return row


def get_responsabilidade():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM v_RESPONSABILIDADE")
    row = cursor.fetchall()
    return row


import datetime


# Retorna quantidade de atendimentos que ocorreram nos
# ultimos trinta dias

def get_qtd_atendimento_no_ultimo_mes():
    today = datetime.datetime.now()
    lastMonth = today - datetime.timedelta(days=30)

    cursor = connection.cursor()
    sqlquery= "SELECT COUNT(id_atendimentocuidador) FROM atendimentocuidador WHERE atendimentocuidador.datahorainicio > %s::timestamp without time zone;"
    cursor.execute(sqlquery, (lastMonth,))
    row = cursor.fetchall()
    return row[0][0]

def get_medicos():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM v_detalhesmedico ORDER BY nome")
    row = cursor.fetchall()
    return row

def get_contratos():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_DETALHECONTRATO ORDER BY datainicio DESC")
    row = cursor.fetchall()
    return row

def get_contratos_por_id(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_DETALHECONTRATO WHERE id_contrato=%s", (id,))
    row = cursor.fetchall()
    return row[0]


def get_atendimentos():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM v_DetalheAtendimentoCuidador")
    row = cursor.fetchall()
    return row

def get_pacienteadulto():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pacienteadulto")
    row = cursor.fetchall()
    return row

def get_paciente_by_id(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTE WHERE id_paciente = %s", (id,))
    row = cursor.fetchall()
    return row[0]

def get_detalhes_pacienteadulto():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_DETALHES_PACIENTEADULTO")
    row = cursor.fetchall()
    return row

def get_detalhes_pacienteadulto_bycpf(cpf):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_DETALHES_PACIENTEADULTO WHERE cpf = %s", (cpf,))
    row = cursor.fetchall()
    return row[0]

def get_planosdeatendimento():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM planoatendimento order by dataplano desc")
    row = cursor.fetchall()
    return row

def get_nroatendimentos_plano(id):
    cursor = connection.cursor()
    cursor.execute("SELECT nro_atendimentos(id_planoatendimento) FROM planoatendimento WHERE id_planoatendimento = %s", (id,))
    row = cursor.fetchall()
    return row[0]

def get_atividadeprevista_id(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM atividadeprevista WHERE fk_id_planoatendimento = %s", (id,))
    row = cursor.fetchall()
    return row

def get_nroatividadeprevista_plano(id):
    cursor = connection.cursor()
    cursor.execute("SELECT nro_atividadeprevista(id_planoatendimento) FROM planoatendimento WHERE id_planoatendimento = %s", (id,))
    row = cursor.fetchall()
    return row[0]

def get_atendimento_por_id(id):
    id = str(id)
    dados_do_atendimento = {}

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM v_DetalheAtendimentoCuidador WHERE id_atendimentocuidador = %s", (id,))
    dados_do_atendimento['atendimento'] = cursor.fetchall()[0]

    cursor.execute("SELECT * FROM ATIVIDADE WHERE fk_atendimentocuidador = %s", (id,))
    dados_do_atendimento['atividades'] = cursor.fetchall()

    cursor.execute("SELECT intercorrencia FROM IntercorrenciaAtendimentoCuidador WHERE id_atendimentocuidador = %s", (id,))
    dados_do_atendimento['intercorrencias'] = cursor.fetchall()

    return dados_do_atendimento

def get_medidas_atividade(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM MedidaAtividade WHERE fk_atividade = %s", (id,))
    return cursor.fetchall()

def get_horarios_livres_by_cpf(cpf):
    cursor = connection.cursor()
    sqlquery="SELECT horario_inicio, horario_fim FROM horarioslivrescuidador WHERE cpf_cuidador= %s"
    cursor .execute(sqlquery, (str(cpf),))
    row = cursor.fetchall()
    return row


