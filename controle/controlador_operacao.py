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

    def saque(self, conta, opcao_escolhida):
        saldo_saque = self.__controlador_conta.pega_saldo_por_codigo(conta.codigo)
        valor = self.__tela_operacao.pega_dados_saida(saldo_saque)
        if valor > 0:
            operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, "", "")
            valida_saldo = self.__controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
            if valida_saldo:
                self.__operacoes.append(operacao)
                self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso")

    def deposito(self, conta, opcao_escolhida):
        valor = self.__tela_operacao.pega_dados_deposito()
        operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, "", "")
        valida_saldo = self.__controlador_conta.atualizar_saldo(conta.codigo, valor)
        if valida_saldo:
            self.__operacoes.append(operacao)
            self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso")

    def valida_transferencia(self, conta, conta_destino):
        if conta.tipo != 2 and conta_destino.tipo != 2 or conta.titular == conta_destino.titular:
            if conta_destino.tipo != 3 or conta.tipo == 3 and conta.titular == conta_destino.titular and conta_destino.tipo != 3:
                saldo_transferencia = self.__controlador_conta.pega_saldo_por_codigo(conta.codigo)
                valor = self.__tela_operacao.pega_dados_saida(saldo_transferencia)
                if valor > 0:
                    return True, valor, saldo_transferencia
            else:
                self.__tela_operacao.mostra_mensagem(
                    "\nA conta atual, do tipo salario não permite transferências para outra titularidade!")
                return False, None, None
        else:
            self.__tela_operacao.mostra_mensagem("\nUma das contas envolvidas na transação é do tipo poupança e, por isso, não está apta a realizar/receber essa transferencia, ela apenas podem transferir para mesma titularidade!")
            return False, None, None


    def transferencia(self, conta, opcao_escolhida):
        codigo_conta_destino = self.__tela_operacao.pega_codigo_conta_destino()
        conta_destino = self.__controlador_conta.pega_conta_por_codigo(codigo_conta_destino)
        if conta_destino is not None:
            validacao, valor, saldo_transferencia =  self.valida_transferencia(conta, conta_destino)
            if validacao:
                operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, conta_destino, '')
                if valor <= 1000 and saldo_transferencia >= valor + 2:
                    valida_saldo_enviado = self.__controlador_conta.atualizar_saldo(conta.codigo, ((valor + 2.0) * (-1)))
                elif valor > 1000 and saldo_transferencia >= valor + 3:
                    valida_saldo_enviado = self.__controlador_conta.atualizar_saldo(conta.codigo, ((valor + 3.0) * (-1)))
                else:
                    self.__tela_operacao.mostra_mensagem("\nVocê não possui saldo suficiente para essa transferência!")
                    valida_saldo_enviado = False
                if valida_saldo_enviado:
                    valida_saldo_recebido = self.__controlador_conta.atualizar_saldo(conta_destino.codigo, valor)
                    if valida_saldo_recebido:
                        self.__operacoes.append(operacao)
                        self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso")
        else:
            self.__tela_operacao.mostra_mensagem("\nO código da conta é invélido ou incorreto!")

    def transferencia_PIX(self, conta, opcao_escolhida):
        chave_PIX = self.__tela_operacao.pega_chave_PIX()
        conta_destino = self.__controlador_conta.pega_conta_por_chave_PIX(chave_PIX)
        if conta_destino is not None:
            validacao, valor, saldo_transferencia = self.valida_transferencia(conta, conta_destino)
            if validacao:
                operacao = Operacao(conta, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), valor, conta_destino, chave_PIX)
                valida_saldo_enviado = self.__controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
                if valida_saldo_enviado:
                    valida_saldo_recebido = self.__controlador_conta.atualizar_saldo(conta_destino.codigo, valor)
                    if valida_saldo_recebido:
                        self.__operacoes.append(operacao)
                        self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso")
        else:
            self.__tela_operacao.mostra_mensagem("\nA chave PIX é invalida ou incorreta!")

    def consultar_extrato(self, conta, opcao_escolhida):
        self.__tela_operacao.mostra_mensagem(f'Saldo da conta: R${conta.saldo}\n')
        self.__tela_operacao.mostra_mensagem(f'Conta Operação               Data         Horário   Valor  \n')
        for operacao in self.__operacoes:
            if operacao.conta == conta:
                data = operacao.data_operacao
                tipo_operacao = operacao.tipo
                if tipo_operacao == self.TIPOS_OPERACOES[1] or tipo_operacao == self.TIPOS_OPERACOES[2]:
                    dados_operacao = {"Codigo": operacao.conta.codigo, "Tipo": tipo_operacao.ljust(21), "Data": data.strftime("%b %d %Y %H:%M:%S"), "Valor": operacao.valor,  "Conta_destino": operacao.conta_destino, "Chave": operacao.chave}
                else:
                    dados_operacao = {"Codigo": operacao.conta.codigo, "Tipo": tipo_operacao,
                                      "Data": data.strftime("%b %d %Y %H:%M:%S"), "Valor": operacao.valor, "Conta_destino": operacao.conta_destino.codigo, "Chave": operacao.chave}
                self.__tela_operacao.exibe_extrato(dados_operacao)

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
