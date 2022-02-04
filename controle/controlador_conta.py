from limite.tela_conta import TelaConta
from controle.controlador_operacao import ControladorOperacao
from entidade.conta import Conta

import random

class ControladorConta:

    def __init__(self, controlador_sistema):
        self.__contas = []
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
        cliente = self.__controlador_sistema.retorna_cliente(dados_conta["cpf_titular"])
        if cliente is not None:
            conta = Conta(codigo, cliente,  dados_conta["tipo_conta"], dados_conta["senha_operacoes"])
            self.__contas.append(conta)
            self.__tela_conta.mostra_mensagem("\nConta criada com sucesso!")
            self.__tela_conta.mostra_mensagem(f'O código da sua conta é {codigo}')
        else:
            self.__tela_conta.mostra_mensagem("\nCliente não foi encontrado!")

    def valida_existencia_e_senha_conta(self):
        codigo_conta = self.__tela_conta.seleciona_codigo()
        conta = self.pega_conta_por_codigo(codigo_conta)
        if (conta is not None):
            senha_operacoes = self.__tela_conta.pega_senha_operacoes()
            if conta.senha_operacoes == senha_operacoes:
                return True, conta
            else:
                self.__tela_conta.mostra_mensagem("\nATENÇÃO: Senha incorreta!")
                return False, None
        else:
            self.__tela_conta.mostra_mensagem("\nATENÇÃO: Conta não existente!")
            return False, None

    def excluir_conta(self):
        validacao, conta = self.valida_existencia_e_senha_conta()
        if validacao:
            if (conta.saldo == 0):
                    self.__contas.remove(conta)
                    self.__tela_conta.mostra_mensagem("\nConta excluida com sucesso!")
            else:
                self.__tela_conta.mostra_mensagem(f"\nO saldo atual da conta é de R${conta.saldo}. Para encerrar a conta, saque ou transfira todos os fundos")

    def listar_informacoes_conta(self):
        validacao, conta = self.valida_existencia_e_senha_conta()
        if validacao:
            dados_conta = {"codigo": conta.codigo, "agencia": conta.agencia,
                             "cpf": conta.titular.cpf, "tipo": conta.tipo, "chaves": conta.chaves_PIX}
            self.__tela_conta.lista_conta(dados_conta)


    def cadastrar_PIX(self):
        validacao, conta = self.valida_existencia_e_senha_conta()
        if validacao:
            if conta.tipo != 3:
                chave_PIX = self.__tela_conta.pega_chave_PIX()
                conta.adicionar_chave_PIX(chave_PIX)
                self.__tela_conta.mostra_mensagem("\nChave PIX cadastrada com sucesso!")
            else:
                self.__tela_conta.mostra_mensagem("\nContas do tipo salário não podem cadastar chaves PIX, pois não podem receber transferências")

    def realizar_operacoes(self):
        validacao, conta = self.valida_existencia_e_senha_conta()
        if validacao:
            self.__controlador_operacao.abre_tela(conta)

    def atualizar_saldo(self, codigo_conta, valor):
        conta = self.pega_conta_por_codigo(codigo_conta)
        if (conta is not None):
            if valor < 0:
                senha_operacoes = self.__tela_conta.pega_senha_operacoes()
                if conta.senha_operacoes == senha_operacoes:
                    conta.saldo += valor
                    return True
                else:
                    self.__tela_conta.mostra_mensagem("\nATENÇÃO: Senha incorreta!")
                    return False
            else:
                conta.saldo += valor
                return True

    def pega_conta_por_codigo(self, codigo_conta: int):
        for conta in self.__contas:
            if conta.codigo == codigo_conta:
                return conta
        return None

    def pega_conta_por_chave_PIX(self, chave_PIX):
        for conta in self.__contas:
            for chave in conta.chaves_PIX:
                if chave == chave_PIX:
                    return conta
        return None

    def pega_saldo_por_codigo(self, codigo_conta):
        conta = self.pega_conta_por_codigo(codigo_conta)
        return conta.saldo

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_nova_conta, 2: self.excluir_conta,
                        3: self.listar_informacoes_conta, 4: self.cadastrar_PIX,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_conta.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def listar_contas(self):
        self.__tela_conta.mostra_mensagem("\nLista de Contas\n")
        for conta in self.__contas:
            dados_conta = {"codigo": conta.codigo, "agencia": conta.agencia,
                           "cpf": conta.titular.cpf, "tipo": conta.tipo, "chaves": conta.chaves_PIX}
            self.__tela_conta.lista_conta(dados_conta)

