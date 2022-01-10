from limite.tela_operacao import TelaOperacao

class ControladorOperacao:

    def __init__(self, controlador_sistema):
        self.__tela_operacao = TelaOperacao()
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    def retorno_menu(self):
        self.__controlador_sistema.abre_tela()

    def teste(self):
        print("\nEscolheu uma opção diferente de retornar ao menu anterior\n")

    def abre_tela(self):
        lista_opcoes = {1: self.teste, 2: self.teste, 3: self.teste,
                        4: self.teste, 5: self.teste, 6: self.teste,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_operacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()