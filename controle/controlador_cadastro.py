from limite.tela_cadastro import TelaCadastro

class ControladorCadastro:

    def __init__(self, controlador_sistema):
        self.__tela_cadastro = TelaCadastro()
        self.__controlador_sistema = controlador_sistema

    def retorno_menu(self):
        self.__controlador_sistema.abre_tela()

    def teste(self):
        print("Escolheu uma opção diferente de retornar ao menu anterior")

    def abre_tela(self):
        lista_opcoes = {1: self.teste, 2: self.teste,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_cadastro.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
