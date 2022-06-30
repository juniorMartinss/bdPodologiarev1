import operacoes
import this


def menu():
    print('\Escolha uma das opções abaixo: \n\n'    +
          '1. Cadastrar Colaborador\n'              +
          '2. Cadastrar Paciente\n'                 +
          '3. Cadastrar Estoque de Produtos(R$)\n'  +
          '4. Procedimentos (R$)\n'                 +
          '5. Consultar\n'                          +
          '6. Sair\n'                               )
    this.opcao = int(input())

def operacoes():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe o nome completo do colaborador(a): ')
            nome = input()
            print('Informe o salário do colabrador(a): ')
            salario = input()
            print('informe a dpartamento(função) do colaborador(a): ')
            departamento = input()
            operacoes.inserir(nome, salario, departamento)
        elif this.opcao == 2:
            print('Qual o CPF do paciente(a): ')
            cpf = input()
            print('Qual o nome do paciente(a): ')
            nome = input()
            print('Qual a data de nascimento do paciente(a): ')
            dataDeNascimento = input()
            print('Qual o telefone do paciente(a): ')
            telefone = input()
            print('Qual endereço do paciente(a): ')
            endereco = input()
            print('Qual o CEP do paciente(a): ')
            cep = input()
            operacoes.inserir(cpf, nome, dataDeNascimento, telefone, endereco, cep)
        elif