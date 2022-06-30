import mysql.connector
import ConexaoBD #Classe que faz conexão com o banco de dados

db_connection = ConexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, salario, departamento):
    try:
       sql = "insert into colaborador(codigo, nome, salario, departamento) values('', '{}', '{}', '{}')".format(nome, salario, departamento)
       con.execute(sql)
       db_connection.commit()#Inserção de dado no DB
       print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def

