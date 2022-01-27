from limite.tela_conta import TelaConta
from controle.controlador_operacao import ControladorOperacao
from entidade.conta import Conta

import random

class ControladorConta:

    def __init__(self, controlador_sistema):
        self.__contas = []
        self.__codigo_conta_selecionada = 0
        self.__tela_conta = TelaConta()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_operacao = ControladorOperacao(self)

    @property
    def controlador_operacao(self):
        return self.__controlador_operacao

    def retorno_menu(self):
        self.__controlador_sistema.abre_tela_cadastros()

    def retorno_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    def cadastrar_nova_conta(self):
        codigo = random.randint(1000, 9999)
        dados_conta = self.__tela_conta.pega_dados_conta()
        #Verificar se o cliente já existe
        conta = Conta(codigo, dados_conta["cpf_titular"],  dados_conta["tipo_conta"], dados_conta["senha_conta"])
        self.__contas.append(conta)
        self.__tela_conta.mostra_mensagem("\nConta criada com sucesso!")
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

    def listar_informacoes_conta(self):
        codigo_conta = self.__tela_conta.seleciona_codigo()
        conta = self.pega_conta_por_codigo(codigo_conta)
        if (conta is not None):
            senha_conta = self.__tela_conta.pega_senha_conta()
            if conta.senha_conta == senha_conta:
                dados_conta = {"codigo": conta.codigo, "agencia": conta.agencia,
                                 "cpf": conta.cpf_titular, "tipo": conta.tipo,}
                self.__tela_conta.lista_conta(dados_conta)
            else:
                self.__tela_conta.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_conta.mostra_mensagem("ATENÇÃO: Conta não existente!")

    def realizar_operacoes(self):
        codigo_conta = self.__tela_conta.seleciona_codigo()
        conta = self.pega_conta_por_codigo(codigo_conta)
        if (conta is not None):
            senha_conta = self.__tela_conta.pega_senha_conta()
            if conta.senha_conta == senha_conta:
                self.__conta_selecionada = codigo_conta
                self.__controlador_operacao.abre_tela()
            else:
                self.__tela_conta.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        else:
            self.__tela_conta.mostra_mensagem("ATENÇÃO: Conta não existente!")

    def registrar_operacoes(self, dados_operacao):
        codigo_conta = self.__codigo_conta_selecionada
        conta = self.pega_conta_por_codigo(codigo_conta)
        senha_conta = self.__tela_conta.pega_senha_conta()
        if conta.senha_conta == senha_conta:
            pass
            #essa função deve ser responsavél pela alteração do saldo em conta e gravar o extrato nos dados da conta
        else:
            self.__tela_conta.mostra_mensagem("ATENÇÃO: Senha incorreta!")
        self.__controlador_operacao.abre_tela()

    def pega_conta_por_codigo(self, codigo_conta: int):
        for conta in self.__contas:
            if conta.codigo == codigo_conta:
                return conta
        return None

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_nova_conta, 2: self.excluir_conta, 3: self.listar_informacoes_conta,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_conta.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()