from limite.lib_limite import valida_opcao, cpf_valido, valida_data
from datetime import datetime

class TelaPessoa:
    def tela_opcoes(self):
        self.exibe_menu()
        return valida_opcao([0,1,2])

    def exibe_menu(self):
        print("\n-------- Gerenciamento de Pessoas ---------\n")
        print("Escolha uma das opções abaixo: ")
        print("1 - Gerenciar clientes")
        print("2 - Gerenciar funcionarios")
        print("0 - Retornar para o menu anterior")

    def tela_opcoes_gerencia(self, tipo):
        self.exibe_menu_gerencia(tipo)
        return valida_opcao([0,1,2,3,4])

    def exibe_menu_gerencia(self, tipo):
        print("\n-------- Gerenciamento de", tipo, " ---------\n")
        print("Escolha como deseja gerenciar o", tipo, ": ")
        print("1 - Cadastrar novo", tipo)
        print("2 - Editar", tipo)
        print("3 - Excluir", tipo)
        print("4 - Listar", tipo)
        print("0 - Retornar para o menu anterior")

    def pega_dados_cliente(self):
        print("\n-------- Dados do Cliente ----------\n")
        nome = input("Nome: ")
        while True:
            try:
                data_nascimento_dia = int(input("Informe o dia do seu nascimento: "))
                data_nascimento_mes = int(input("Informe o mês do seu nascimento: "))
                data_nascimento_ano = int(input("Informe o ano do seu nascimento: "))
                if valida_data(data_nascimento_dia, data_nascimento_mes, data_nascimento_ano):
                    data_nascimento_str = f'{data_nascimento_dia}/{data_nascimento_mes}/{data_nascimento_ano}'
                    data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
                    break
                else:
                    print("Parece que a data informada é invalida, tente novamente!")
            except:
                print("Parece que algo deu errado, tente novamente!")
        cpf = cpf_valido()
        senha_cadastro = input("Senha para cadastros: ")

        return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "senha_cadastro": senha_cadastro}

    def pega_dados_cliente_alteracao(self):
        print("\n-------- Dados Atualizados do Cliente ----------\n")
        nome = input("Nome: ")
        senha_cadastro = input("Nova senha para cadastros: ")

        return {"nome": nome, "senha_cadastro": senha_cadastro}

    def pega_dados_funcionario(self):
        print("\n-------- Dados do Funcionário ----------\n")
        nome = input("Nome: ")
        while True:
            try:
                data_nascimento_dia = int(input("Informe o dia do seu nascimento: "))
                data_nascimento_mes = int(input("Informe o mês do seu nascimento: "))
                data_nascimento_ano = int(input("Informe o ano do seu nascimento: "))
                if valida_data(data_nascimento_dia, data_nascimento_mes, data_nascimento_ano):
                    data_nascimento_str = f'{data_nascimento_dia}/{data_nascimento_mes}/{data_nascimento_ano}'
                    data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
                    break
                else:
                    print("Parece que a data informada é invalida, tente novamente!")
            except:
                print("Parece que algo deu errado, tente novamente!")
        cpf = cpf_valido()
        numero_CTPS = input("Número da CTPS: ")
        while len(numero_CTPS)!=8:
            print("Número de documento inválido, deve conter 8 dígitos!")
            numero_CTPS = input("Número da CTPS: ")
        senha_funcionario = input("Senha para cadastros: ")

        return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "numero_CTPS": numero_CTPS, "senha_funcionario": senha_funcionario}

    def pega_dados_funcionario_alteracao(self):
        print("\n-------- Dados Atualizados do Funcionário ----------\n")
        nome = input("Nome: ")
        senha_funcionario = input("Nova senha para cadastros: ")

        return {"nome": nome, "senha_funcionario": senha_funcionario}

    def seleciona_cpf(self):
        return cpf_valido()

    def pega_senha_pessoa(self):
        return input("Digite a sua senha para prosseguir com a operação: ")

    def lista_cliente(self, dados_cliente):
        print("\nCliente:", dados_cliente["codigo"], "-", dados_cliente["nome"])
        print("Data de nascimento do cliente:", dados_cliente["data_nascimento"].strftime('%d/%m/%Y'))
        print(f"CPF do cliente: {str(dados_cliente['cpf'])[0:3]}.{str(dados_cliente['cpf'])[3:6]}.{str(dados_cliente['cpf'])[6:9]}-{str(dados_cliente['cpf'])[9:11]}")

    def lista_funcionario(self, dados_funcionario):
        print("\nFuncionário:", dados_funcionario["codigo"], "-", dados_funcionario["nome"])
        print("Data de nascimento do funcinário:", dados_funcionario["data_nascimento"].strftime('%d/%m/%Y'))
        print(f"CPF do funcionário: {str(dados_funcionario['cpf'])[0:3]}.{str(dados_funcionario['cpf'])[3:6]}.{str(dados_funcionario['cpf'])[6:9]}-{str(dados_funcionario['cpf'])[9:11]}")
        print("Número CTPS do funcinário:", dados_funcionario["numero_CTPS"])

    def mostra_mensagem(self, msg):
        print(msg)