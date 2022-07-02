import operacoes
import this

this.opcao = -1


def menu():
    print('Escolha uma das opções abaixo: \n\n' +
          '1. Cadastrar Colaborador\n' +
          '2. Cadastrar Paciente\n' +
          '3. Cadastrar Estoque de Produtos(R$)\n' +
          '4. Procedimentos (R$)\n' +
          '5. Consultar\n' +
          '0. Sair\n')
    this.opcao = int(input())


def operacoes():
    while (this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe o nome completo do colaborador(a): ')
            nome = input()
            print('Informe o salário do colabrador(a): ')
            salario = input()
            print('Informe a departamento(função) do colaborador(a): ')
            departamento = input()
            print('Informe o telefone: ')
            telefone = input()
            print('Informe a data de nascimento: ')
            dataDeNascimento = input()
            print('Informe o endereço:  ')
            endereco = input()
            print('Informe o CEP: ')
            cep = input()
            print('Precisa de vale transporte?')
            valetransporte = input()
            print('Comentários, observarções, etc. Digite aqui!')
            obs = input()
            operacoes.inserir(nome, salario, departamento, telefone, dataDeNascimento, endereco, cep, valetransporte, obs)
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
        elif this.opcao == 3:
            print('Infome o produto: ')
            produto = input()
            print('Informe o valor do produto: ')
            valor = input()
            print('Informe a quantidade que foi comprada do produto: ')
            quantidade = input()
            print('Informe o fabricante do produto: ')
            fabricante = input()
            print('Informe o fornecedor do produto: ')
            fornecedor = input()
            print('informe a origem do produto (País de fabricação): ')
            origem = input()
            print('Comentários, observarções, etc. Digite aqui!')
            obs = input()
            operacoes.inserir(produto, valor, quantidade, fabricante, fornecedor, origem, obs)
        elif this.opcao == 4:
            print('Informe os procedimentos para cadastrar: ')
            procedimento = input()
            print('Informe do procedimento: ')
            valor = input()
            operacoes.inserir(procedimento, valor)
        else:
            print('Opção escolhida não é válida!')
