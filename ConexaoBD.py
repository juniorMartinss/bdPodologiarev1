import mysql.connector #faz o acesso
from mysql.connector import errorcode #trata as exceções que vão surgir

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bdPodologia')
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as erro: #guardando as possíveis exceções na variável erro
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #caso o banco de dados não exista
            print('Banco de dados não existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACESS_DENIED_ERROR: #caso o usuario ou senha estejam errados
            print('Usuário ou senha nã são válidas!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close()