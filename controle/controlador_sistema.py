from limite.tela_sistema import TelaSistema
from controle.controlador_cadastro import ControladorCadastro

class ControladorSistema:

    def __init__(self,):
        self.__tela_sistema = TelaSistema()
        self.__controlador_cadastro = ControladorCadastro(self)

    @property
    def controlador_cadastro(self):
        return self.__controlador_cadastro

    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def teste(self):
        print("Escolheu uma opção diferente de encerrar o sistema")

    def gerenciar_cadastros(self):
        self.__controlador_cadastro.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerenciar_cadastros, 2: self.teste, 3: self.teste,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
