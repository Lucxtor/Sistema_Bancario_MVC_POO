from limite.lib_limite import valida_opcao, cpf_valido

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
        print("-------- Dados do Cliente ----------")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = cpf_valido()
        senha_operacoes = input("Senha para operações: ")

        return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "senha_operacoes": senha_operacoes}

    def pega_dados_cliente_alteracao(self):
        print("-------- Dados Atualizados do Cliente ----------")
        nome = input("Nome: ")
        senha_operacoes = input("Senha para operações: ")

        return {"nome": nome, "senha_operacoes": senha_operacoes}

    def pega_dados_funcionario(self):
        print("-------- Dados do Funcionário ----------")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = cpf_valido()
        numero_CTPS = input("Número da CTPS: ")
        senha_funcionario = input("Senha para operações: ")

        return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "numero_CTPS": numero_CTPS, "senha_funcionario": senha_funcionario}

    def pega_dados_funcionario_alteracao(self):
        print("-------- Dados Atualizados do Funcionário ----------")
        nome = input("Nome: ")
        senha_funcionario = input("Senha para operações: ")

        return {"nome": nome, "senha_funcionario": senha_funcionario}



    def pega_senha_pessoa(self):
        return input("Digite a sua senha para prosseguir com a operação: ")

    def lista_cliente(self, dados_cliente):
        print("Cliente:", dados_cliente["codigo"], "-", dados_cliente["nome"])
        print("Data de nascimento do cliente:", dados_cliente["data_nascimento"])
        print("CPF do cliente:", str(dados_cliente["cpf"])[0:3], ".", str(dados_cliente["cpf"])[3:6], ".", str(dados_cliente["cpf"])[6:9], "-", str(dados_cliente["cpf"])[9:11])
        print()

    def lista_funcionario(self, dados_funcionario):
        print("Funcionário:", dados_funcionario["codigo"], "-", dados_funcionario["nome"])
        print("Data de nascimento do funcinário:", dados_funcionario["data_nascimento"])
        print("CPF do funcinário:", str(dados_funcionario["cpf"])[0:3], ".", str(dados_funcionario["cpf"])[3:6], ".", str(dados_funcionario["cpf"])[6:9], "-", str(dados_funcionario["cpf"])[9:11])
        print("Número CTPS do funcinário", dados_funcionario["numero_CTPS"])
        print()

    def mostra_mensagem(self, msg):
        print(msg)