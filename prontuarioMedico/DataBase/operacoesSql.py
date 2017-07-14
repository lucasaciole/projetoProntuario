from django.db import connection, transaction

# If using cursor without "with" -- it must be closed explicitly:
# with connection.cursor() as cursor:
#     cursor.execute('select * from table where aaa=%s', [5])
#     for row in cursor.fetchall():
#         print(str(row[0]) + str(row[1]) + str(row[3]))

def teste():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM PACIENTE")

    for row in cursor.fetchall():
        print(str(row[0]) + str(row[1]) + str(row[2]))