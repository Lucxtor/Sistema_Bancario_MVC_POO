from limite.tela_conta import TelaConta
import random
from entidade.conta import Conta

class ControladorConta:

    def __init__(self, controlador_cadastro):
        self.__contas = []
        self.__tela_conta = TelaConta()
        self.__controlador_cadastro = controlador_cadastro


    def retorno_menu(self):
        self.__controlador_cadastro.abre_tela()

    def teste(self):
        print("\nEscolheu uma opção diferente de retornar ao menu anterior\n")

    def cadastrar_nova_conta(self):
        codigo = random.randint(1000, 9999)
        dados_conta = self.__tela_conta.pega_dados_conta()
        #Verificar se o cliente já existe
        conta = Conta(codigo, dados_conta["cpf_titular"],  dados_conta["tipo_conta"], dados_conta["senha_conta"])
        self.__contas.append(conta)
        self.__tela_conta.mostra_mensagem("Conta criada com sucesso!")
        self.__tela_conta.mostra_mensagem(f'O código da sua conta é {codigo}')

    def excluir_conta(self):
        codigo_conta = self.__tela_conta.seleciona_codigo()
        conta = self.pega_conta_por_codigo(codigo_conta)
        if (conta is not None):
            senha_conta = self.__tela_conta.pega_senha_conta()
            if conta.senha_conta == senha_conta:
                self.__contas.remove(conta)
                self.__tela_conta.mostra_mensagem("Conta excluida com sucesso!")
            else:
                self.__tela_conta.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_conta.mostra_mensagem("ATENÇÃO: Conta não existente!")

    def listar_informacoes(self):
        pass

    def pega_conta_por_codigo(self, codigo_conta: int):
        for conta in self.__contas:
            if conta.codigo1 == codigo_conta:
                return conta
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_nova_conta, 2: self.excluir_conta, 3:self.listar_informacoes,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_conta.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()