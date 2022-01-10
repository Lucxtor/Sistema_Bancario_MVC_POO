from limite.tela_sistema import TelaSistema
from controle.controlador_cadastro import ControladorCadastro
from controle.controlador_operacao import ControladorOperacao


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cadastro = ControladorCadastro(self)
        self.__controlador_operacao = ControladorOperacao(self)

    @property
    def controlador_cadastro(self):
        return self.__controlador_cadastro

    @property
    def controlador_operacao(self):
        return self.__controlador_operacao

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def teste(self):
        print("\nEscolheu uma opção diferente de encerrar o sistema\n")

    def gerenciar_cadastros(self):
        self.__controlador_cadastro.abre_tela()

    def realizar_operacoes(self):
        self.__controlador_operacao.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerenciar_cadastros, 2: self.realizar_operacoes, 3: self.teste,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()