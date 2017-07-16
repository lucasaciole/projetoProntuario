from django.db import connection, transaction

# Consultas de quantidades
def get_valores_home():
    cursor = connection.cursor()
    cursor.execute("SELECT dados_para_home()")
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