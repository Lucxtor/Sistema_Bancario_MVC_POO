from limite.tela_cadastro import TelaCadastro
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_conta import ControladorConta

class ControladorCadastro:

    def __init__(self, controlador_sistema):
        self.__tela_cadastro = TelaCadastro()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_pessoa = ControladorPessoa(self)

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    def retorno_menu(self):
        self.__controlador_sistema.abre_tela()

    def gerenciar_pessoas(self):
        self.__controlador_pessoa.abre_tela()

    def gerenciar_contas(self):
        self.__controlador_conta.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerenciar_pessoas, 2: self.gerenciar_contas,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_cadastro.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()