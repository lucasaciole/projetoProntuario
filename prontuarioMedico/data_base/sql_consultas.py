from django.db import connection, transaction

def teste():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTE")

    for row in cursor.fetchall():
        print(str(row[0]) + str(row[1]) + str(row[2]))

# Consultas de quantidades
def get_qtd_pacientes():
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id_paciente) FROM PACIENTE")
    row = cursor.fetchall()
    return row[0][0]

def get_qtd_medicos():
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(?) FROM MEDICO")
    row = cursor.fetchall()
    return row[0][0]

def get_qtd_cuidadores():
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(cpf_cuidador) FROM CUIDADOR")
    row = cursor.fetchall()
    return row[0][0]

def get_qtd_responsabilidades():
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id_paciente) FROM v_Responsabilidade")
    row = cursor.fetchall()
    return row[0][0]

# Consultas de tabelas
def get_cuidador():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_CUIDADOR")
    row = cursor.fetchall()
    return row

def get_paciente():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTE")
    row = cursor.fetchall()
    return row

#Retorna todos pacientes que possuem 'nome' como substring (case insensitive)
def get_pacientes_por_nome(nome ):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTE WHERE LOWER(nome) LIKE LOWER(\'%"+str(nome)+"%\')")
    row = cursor.fetchall()
    return row

def get_responsabilidade():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM v_RESPONSABILIDADE")
    row = cursor.fetchall()
    return row
import datetime

#Retorna quantidade de atendimentos que ocorreram nos
#ultimos trinta dias

def get_qtd_atendimento_no_ultimo_mes():
    today = datetime.date.today()
    lastMonth = today - datetime.timedelta(days=30)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id_atendimentocuidador) FROM atendimentocuidador WHERE atendimentocuidador.datahorainicio > \'"+str(lastMonth.year)+"-"+str(lastMonth.month)+"-"+str(lastMonth.day)+"\'::timestamp without time zone")
    row = cursor.fetchall()
    return row[0][0]