from datetime import datetime

from entidade.cliente import Cliente
from limite.tela_conta import TelaConta
from entidade.conta import Conta

import random

cliente01 = Cliente(10, "Teste 01", datetime.strptime('09/06/2002', '%d/%m/%Y'), 99999999999, '123')
cliente02 = Cliente(11, "Teste 02", datetime.strptime('09/06/2002', '%d/%m/%Y'), 88888888888, '123')
conta01 = Conta(1111, cliente01, 1, '123')
conta02 = Conta(1222, cliente01, 1, '123')
conta03 = Conta(1333, cliente01, 2, '123')
conta04 = Conta(1444, cliente01, 2, '123')
conta05 = Conta(1555, cliente01, 3, '123')
conta06 = Conta(1666, cliente01, 3, '123')
conta07 = Conta(2111, cliente02, 1, '123')
conta08 = Conta(2222, cliente02, 2, '123')
conta09 = Conta(2333, cliente02, 3, '123')
conta01.adicionar_chave_PIX('chave0101')
conta03.adicionar_chave_PIX('chave0102')
conta07.adicionar_chave_PIX('chave0201')
conta08.adicionar_chave_PIX('chave0202')
precadastroContas = [conta01, conta02, conta03, conta04, conta05, conta06, conta07, conta08, conta09]

class ControladorConta:

    def __init__(self, controlador_sistema):
        #self.__contas = []
        self.__contas = precadastroContas
        self.__tela_conta = TelaConta()
        self.__controlador_sistema = controlador_sistema

    def retorno_menu(self):
        self.__controlador_sistema.abre_tela_cadastros()

    def retorno_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    def cadastrar_nova_conta(self):
        codigo = random.randint(1000, 9999)
        dados_conta = self.__tela_conta.pega_dados_conta()
        cliente = self.__controlador_sistema.controlador_pessoa.pega_cliente_por_cpf(dados_conta["cpf_titular"])
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
            #Regra de Negócio: Para que uma conta seja excluída, ela deve estar com um saldo de 0 reais
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
        # Regras de Negócio: As transferências, saques e consultas a uma determinada conta só podem ocorrer mediante senha do Titular.
        if validacao:
            self.__controlador_sistema.controlador_operacao.abre_tela(conta)

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
        self.__tela_conta.mostra_mensagem("\nLista de Contas")
        for conta in self.__contas:
            dados_conta = {"codigo": conta.codigo, "agencia": conta.agencia,
                           "cpf": conta.titular.cpf, "tipo": conta.tipo, "chaves": conta.chaves_PIX}
            self.__tela_conta.lista_conta(dados_conta)

