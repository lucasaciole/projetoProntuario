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
    return row


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