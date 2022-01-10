from limite.tela_conta import TelaConta

class ControladorConta:

    def __init__(self, controlador_cadastro):
        self.__tela_conta = TelaConta()
        self.__controlador_cadastro = controlador_cadastro

    def retorno_menu(self):
        self.__controlador_cadastro.abre_tela()

    def teste(self):
        print("\nEscolheu uma opção diferente de retornar ao menu anterior\n")

    def cadastrar_nova_conta(self):
        pass

    def excluir_conta(self):
        pass

    def listar_informacoes(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_nova_conta, 2: self.excluir_conta, 3:self.listar_informacoes,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_conta.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()