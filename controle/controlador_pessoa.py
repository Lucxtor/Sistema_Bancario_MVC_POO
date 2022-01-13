from limite.tela_pessoa import TelaPessoa

class ControladorPessoa:

    def __init__(self, controlador_cadastro):
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_cadastro = controlador_cadastro

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
        lista_opcoes_cliente = {1: self.teste, 2: self.teste, 3: self.teste,
                                0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes_cliente()
            funcao_escolhida = lista_opcoes_cliente[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_funcionario(self):
        lista_opcoes_funcionario = {1: self.teste, 2: self.teste, 3: self.teste,
                                    0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes_funcionario()
            funcao_escolhida = lista_opcoes_funcionario[opcao_escolhida]
            funcao_escolhida()
