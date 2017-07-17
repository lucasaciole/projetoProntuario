from django.db import connection

def inserir_cuidador(form):
    cursor = connection.cursor()
    insert = "insert into v_detalhes_cuidador(cpf_cuidador, nome, tipocuidador, datanascimento, logradouro, numero, complemento, bairro, cidade, estado, cep, rg)"
    insert += "values (%s, %s, %s, to_date(%s, 'yyyy-mm-dd'), %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert, (form['cpf_cuidador'], form['nome'], form['tipoCuidador'], form['datanascimento'], form['logradouro'], form['numero'], form['complemento'], form['bairro'], form['cidade'], form['estado'], form['cep'], form['rg']))
    return cursor.statusmessage

def inserir_contrato(form):
    cursor = connection.cursor()
    print(form)
    insert_str = "insert into contrato(cpf_paciente, cpf_cuidador, datainicio, datafim, tipoatendimento, diavencimento, valoratendimento, periodicidade) "
    insert_str += "values (%s, %s, to_date(%s, 'dd/mm/yyyy'), to_date(%s, 'dd/mm/yyyy'), %s, %s, %s, %s)"
    cursor.execute(insert_str, (form['cpf_paciente'], form['cpf_cuidador'], form['datainicio'], form['datafim'], form['tipoatendimento'], form['diavencimento'], form['valoratendimento'], form['periodicidade']))
    return cursor.statusmessage