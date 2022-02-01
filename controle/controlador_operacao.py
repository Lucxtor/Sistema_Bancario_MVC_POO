from limite.tela_operacao import TelaOperacao
from entidade.operacao import Operacao

from datetime import datetime

class ControladorOperacao:
    TIPOS_OPERACOES = {1: "Saque", 2: "Depósito", 3: "Transferência Ted/Doc", 4: "Transferência PIX"}
    def __init__(self, controlador_conta):
        self.__operacoes = []
        self.__tela_operacao = TelaOperacao()
        self.__controlador_conta = controlador_conta

    def retorno_menu(self):
        self.__controlador_conta.retorno_menu_principal()

    def teste(self):
        print("\nEscolheu uma opção diferente de retornar ao menu anterior\n")

    def saque(self, conta, opcao_escolhida):
        saldo_saque = self.__controlador_conta.pega_saldo_por_codigo(conta.codigo)
        valor = self.__tela_operacao.pega_dados_saida(saldo_saque)
        operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, "", "")
        self.__controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
        self.__operacoes.append(operacao)
        self.__tela_operacao.mostra_mensagem("Operação realizada com sucesso")

    def deposito(self, conta, opcao_escolhida):
        valor = self.__tela_operacao.pega_dados_deposito()
        operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, "", "")
        self.__controlador_conta.atualizar_saldo(conta.codigo, valor)
        self.__operacoes.append(operacao)
        self.__tela_operacao.mostra_mensagem("Operação realizada com sucesso")

    def transferencia(self, conta, opcao_escolhida):
        codigo_conta_destino = self.__tela_operacao.pega_codigo_conta_destino()
        conta_destino = self.__controlador_conta.pega_conta_por_codigo(codigo_conta_destino)
        if conta_destino is not None:
            saldo_transferencia = self.__controlador_conta.pega_saldo_por_codigo(conta.codigo)
            valor = self.__tela_operacao.pega_dados_saida(saldo_transferencia)
            operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, conta_destino, '')
            self.__controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
            self.__controlador_conta.atualizar_saldo(conta_destino.codigo, valor)
            self.__operacoes.append(operacao)
            self.__tela_operacao.mostra_mensagem("Operação realizada com sucesso")
        else:
            self.__tela_operacao.mostra_mensagem("O código da conta é invalido ou incorreto!")

    def transferencia_PIX(self, conta, opcao_escolhida):
        chave_PIX = self.__tela_operacao.pega_chave_PIX()
        conta_destino = self.__controlador_conta.pega_conta_por_chave_PIX(chave_PIX)
        if conta_destino is not None:
            saldo_transferencia = self.__controlador_conta.pega_saldo_por_codigo(conta.codigo)
            valor = self.__tela_operacao.pega_dados_saida(saldo_transferencia)
            operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, conta_destino, chave_PIX)
            self.__controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
            self.__controlador_conta.atualizar_saldo(conta_destino.codigo, valor)
            self.__operacoes.append(operacao)
            self.__tela_operacao.mostra_mensagem("Operação realizada com sucesso")
        else:
            self.__tela_operacao.mostra_mensagem("A chave PIX é invalida ou incorreta!")

    def consultar_extrato(self, conta, opcao_escolhida):
        for i in range(len(self.__operacoes)):
            print(self.__operacoes[i].conta.codigo, self.__operacoes[i].tipo, self.__operacoes[i].data_operacao, self.__operacoes[i].valor, self.__operacoes[i].conta_destino, self.__operacoes[i].chave)

    def consultar_saldo(self, conta, opcao_escolhida):
        saldo_final = self.__controlador_conta.pega_saldo_por_codigo(conta.codigo)
        saldo_depositos = 0
        saldo_saques = 0
        saldo_transferencia_enviadas = 0
        saldo_transferencia_recebidas = 0
        for operacao in self.__operacoes:
            if operacao.conta == conta:
                if operacao.tipo == self.TIPOS_OPERACOES[1]:
                    saldo_saques += operacao.valor
                elif operacao.tipo == self.TIPOS_OPERACOES[2]:
                    saldo_depositos += operacao.valor
                else:
                    saldo_transferencia_enviadas += operacao.valor
            elif operacao.conta_destino == conta:
                saldo_transferencia_recebidas += operacao.valor
        saldo_transferencia_entrada_vs_saida = saldo_transferencia_recebidas - saldo_transferencia_enviadas
        self.__tela_operacao.exibe_saldo(saldo_final, saldo_depositos, saldo_saques, saldo_transferencia_enviadas, saldo_transferencia_recebidas, saldo_transferencia_entrada_vs_saida)

    def abre_tela(self, conta):
        lista_opcoes = {1: self.saque, 2: self.deposito, 3: self.transferencia,
                        4: self.transferencia_PIX, 5: self.consultar_extrato, 6: self.consultar_saldo,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_operacao.tela_opcoes(conta.agencia, conta.codigo)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if opcao_escolhida != 0:
                funcao_escolhida(conta, opcao_escolhida)
            else:
                funcao_escolhida()
