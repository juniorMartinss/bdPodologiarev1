import mysql.connector
import ConexaoBD  # Classe que faz conexão com o banco de dados

db_connection = ConexaoBD.conectar()
con = db_connection.cursor()


def inserirColaborador(nome, salario, departamento, telefone, dataDeNascimento, endereco, cep, valetransporte, obs):
    try:
        sql = "insert into colaborador(codigo, nome, salario, departamento, telefone, dataDeNascimento, endereco, cep, valeTransporte, obs) values('', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nome, salario, departamento, telefone, dataDeNascimento, endereco, cep, valetransporte, obs)
        con.execute(sql)
        db_connection.commit()  # Inserção de dado no DB
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def tratarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)


def inserirPaciente(cpf, nome, datadeNascimento, telefone, endereco, cep):
    try:
        sql = "insert into paciente(cpf, nome, dataDeNascimento, telefone, endereco, cep) values('{}', '{}', '{}', '{}', '{}', '{}')".format(cpf, nome, datadeNascimento, telefone, endereco, cep)
        con.execute(sql)
        db_connection.commit()  # Inserção de dado no DB
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro



def inserirEstoque(produto, valor, quantidade, fabricante, fornecedor, origem, obs):
    try:
        sql = "insert into estoque(codigo, produto, valor, quantidade, fabricante, fornecedor, origem, obs) values('', '{}', '{}', '{}', '{}', '{}', '{}', '{})".format(produto, valor, quantidade, fabricante, fornecedor, origem, obs)
        con.execute(sql)
        db_connection.commit()  # Inserção de dado no DB
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro


def inserirProcedimento(procedimento, valor):
    try:
        sql = "insert into procedimento(codigo, procedimento, valor) values('', '{}', '{}')".format(procedimento, valor)
        con.execute(sql)
        db_connection.commit()  # Inserção de dado no DB
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

