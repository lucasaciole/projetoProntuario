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

def get_cuidador():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM V_CUIDADOR")
    row = cursor.fetchall()
    return row