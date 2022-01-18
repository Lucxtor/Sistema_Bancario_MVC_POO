from limite.tela_pessoa import TelaPessoa
from entidade.cliente import Cliente

class ControladorPessoa:

    def __init__(self, controlador_cadastro):
        self.__clientes = []
        self.__funcionarios = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_cadastro = controlador_cadastro

    def incluir_cliente(self):
        codigo = len(self.__clientes) + 1
        dados_cliente = self.__tela_pessoa.pega_dados_cliente()
        cliente = Cliente(codigo, dados_cliente["nome"], dados_cliente["data_nascimento"], dados_cliente["cpf"], dados_cliente["senha_contas"])
        self.__clientes.append(cliente)

    def incluir_funcionario(self):
        codigo = len(self.__funcionarios) + 1
        dados_funcionario = self.__tela_pessoa.pega_dados_funcionario()
        cliente = Cliente(codigo, dados_funcionario["nome"], dados_funcionario["data_nascimento"], dados_funcionario["cpf"], dados_funcionario["numero_CTPS"], dados_funcionario["senha_funcionario"])
        self.__clientes.append(cliente)

    def retorno_menu(self):
        self.__controlador_cadastro.abre_tela()

    def teste(self):
        print("\nEscolheu uma opção diferente de retornar ao menu anterior\n")

    def abre_tela(self):
        lista_opcoes = {1: self.abre_tela_cliente, 2: self.abre_tela_funcionario,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_cliente(self):
        lista_opcoes_cliente = {1: self.incluir_cliente, 2: self.teste, 3: self.teste,
                                0: self.abre_tela}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes_gerencia('cliente')
            funcao_escolhida = lista_opcoes_cliente[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_funcionario(self):
        lista_opcoes_funcionario = {1: self.incluir_funcionario, 2: self.teste, 3: self.teste,
                                    0: self.abre_tela}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes_gerencia('funcionário')
            funcao_escolhida = lista_opcoes_funcionario[opcao_escolhida]
            funcao_escolhida()
