from limite.tela_operacao import TelaOperacao
from entidade.operacao import Operacao
from persistencia.operacao_dao import OperacaoDAO

from datetime import datetime

class ControladorOperacao:
    TIPOS_OPERACOES = {1: "Saque", 2: "Depósito", 3: "Transferência Ted/Doc", 4: "Transferência PIX"}
    def __init__(self, controlador_sistema):
        self.__operacao_dao = OperacaoDAO()
        self.__tela_operacao = TelaOperacao()
        if len(self.__operacao_dao.get_all()) != 0:
            self.__codigo_operacao = list(self.__operacao_dao.get_all())[len(self.__operacao_dao.get_all())-1].codigo
        else:
            self.__codigo_operacao = 0
        self.__controlador_sistema = controlador_sistema

    def retorno_menu(self):
        self.__controlador_sistema.controlador_conta.retorno_menu_principal()

    def saque(self, conta, opcao_escolhida):
        saldo_saque = self.__controlador_sistema.controlador_conta.pega_saldo_por_codigo(conta.codigo)
        valor = self.__tela_operacao.pega_dados_saida(saldo_saque)
        if valor is not None:
            self.__codigo_operacao += 1
            operacao = Operacao(self.__codigo_operacao, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now())
            operacao.adicionar_movimentacao(conta, (valor * -1), "Saída")
            valida_saldo = self.__controlador_sistema.controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
            if valida_saldo:
                self.__operacao_dao.add(operacao)
                self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso!")

    def deposito(self, conta, opcao_escolhida):
        while True:
            valor = self.__tela_operacao.pega_dados_deposito()
            if valor == 'Cancel':
                self.__tela_operacao.close()
                self.abre_tela(conta)
            try:
                self.__tela_operacao.close()
                valor = int(valor)
                break
            except:
                self.__tela_operacao.mostra_mensagem("A opção digitada é inválida, por favor, tente novamente!")
        self.__codigo_operacao += 1
        operacao = Operacao(self.__codigo_operacao, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now())
        operacao.adicionar_movimentacao(conta, valor, "Entrada")
        valida_saldo = self.__controlador_sistema.controlador_conta.atualizar_saldo(conta.codigo, valor)
        if valida_saldo:
            self.__operacao_dao.add(operacao)
            self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso!")

    def valida_transferencia(self, conta, conta_destino):
        if conta.codigo != conta_destino.codigo:
            #Regra de Negócio: Contas do tipo poupança não podem fazer ou receber transferências de contas com outra titularidade
            if conta.tipo != 2 and conta_destino.tipo != 2 or conta.titular == conta_destino.titular:
                #Regra de Negócio: Contas Salário apenas permite a transferência para uma conta corrente ou poupança de mesma titularidade ou saques.
                if conta_destino.tipo != 3 and conta.tipo != 3 or conta.tipo == 3 and conta.titular == conta_destino.titular and conta_destino.tipo != 3:
                    saldo_transferencia = self.__controlador_sistema.controlador_conta.pega_saldo_por_codigo(conta.codigo)
                    valor = self.__tela_operacao.pega_dados_saida(saldo_transferencia)
                    if valor is not None:
                        return True, valor, saldo_transferencia
                    else:
                        return False, None, None
                else:
                    self.__tela_operacao.mostra_mensagem(
                        "\nUma das contas envolvidas na transação é do tipo salário e,\npor isso, não está apta a realizar/receber essa transferencia.\nContas salário só podem transferir para contas de mesma titularidade")
                    return False, None, None
            else:
                self.__tela_operacao.mostra_mensagem("\nUma das contas envolvidas na transação é do tipo poupança e,\npor isso, não está apta a realizar/receber essa transferencia.\nContas poupança apenas podem transferir para/receber de contas de mesma titularidade!")
                return False, None, None
        else:
            self.__tela_operacao.mostra_mensagem("\nNão se pode enviar uma transferência para essa mesma conta!")
            return False, None, None

    def transferencia(self, conta, opcao_escolhida):
        codigo_conta_destino = self.__tela_operacao.pega_codigo_conta_destino()
        if codigo_conta_destino == 'Cancel':
            self.abre_tela(conta)
        conta_destino = self.__controlador_sistema.controlador_conta.pega_conta_por_codigo(codigo_conta_destino)
        if conta_destino is not None:
            validacao, valor, saldo_transferencia = self.valida_transferencia(conta, conta_destino)
            if validacao:
                #Transformar entrada e saída em variáveis
                self.__codigo_operacao += 1
                operacao = Operacao(self.__codigo_operacao, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now())
                operacao.adicionar_movimentacao(conta, (valor * -1), "Saída")
                operacao.adicionar_movimentacao(conta_destino, valor, "Entrada")
                if self.calcula_e_adiciona_taxa(valor, saldo_transferencia, conta, operacao):
                    valida_saldo_recebido = self.__controlador_sistema.controlador_conta.atualizar_saldo(
                    conta_destino.codigo, valor)
                    if valida_saldo_recebido:
                        self.__operacao_dao.add(operacao)
                        self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso!")

        else:
            self.__tela_operacao.mostra_mensagem("\nO código da conta é inválido ou incorreto!")


    def calcula_e_adiciona_taxa(self, valor, saldo_transferencia, conta, operacao):
        if valor <= 1000 and saldo_transferencia >= valor + 2:
            valida_saldo_enviado = self.__controlador_sistema.controlador_conta.atualizar_saldo(conta.codigo,((valor + 2.0) * (-1)))
            operacao.adicionar_movimentacao(conta, (-2), "Taxa")
            return valida_saldo_enviado
        elif valor > 1000 and saldo_transferencia >= valor + 3:
            valida_saldo_enviado = self.__controlador_sistema.controlador_conta.atualizar_saldo(conta.codigo,((valor + 3.0) * (-1)))
            operacao.adicionar_movimentacao(conta, (-3), "Taxa")
            return valida_saldo_enviado
        else:
            self.__tela_operacao.mostra_mensagem("\nVocê não possui saldo suficiente para essa transferência!")
            valida_saldo_enviado = False
            return valida_saldo_enviado

    def transferencia_PIX(self, conta, opcao_escolhida):
        chave_PIX = self.__tela_operacao.pega_chave_PIX()
        self.__tela_operacao.close()
        if chave_PIX == 'Cancel':
            self.abre_tela(conta)
        conta_destino = self.__controlador_sistema.controlador_conta.pega_conta_por_chave_PIX(chave_PIX)
        if conta_destino is not None:
            validacao, valor, saldo_transferencia = self.valida_transferencia(conta, conta_destino)
            if validacao:
                self.__codigo_operacao += 1
                operacao = Operacao(self.__codigo_operacao, self.TIPOS_OPERACOES[opcao_escolhida], datetime.now(), chave_PIX)
                operacao.adicionar_movimentacao(conta, (valor * -1), "Saída")
                operacao.adicionar_movimentacao(conta_destino, valor, "Entrada")
                valida_saldo_enviado = self.__controlador_sistema.controlador_conta.atualizar_saldo(conta.codigo, (valor * (-1)))
                if valida_saldo_enviado:
                    valida_saldo_recebido = self.__controlador_sistema.controlador_conta.atualizar_saldo(conta_destino.codigo, valor)
                    if valida_saldo_recebido:
                        self.__operacao_dao.add(operacao)
                        self.__tela_operacao.mostra_mensagem("\nOperação realizada com sucesso!")
        else:
            self.__tela_operacao.mostra_mensagem("\nA chave PIX informada é inválida ou incorreta!")

    def consultar_extrato(self, conta, opcao_escolhida):
        operacoes = []
        for operacao in self.__operacao_dao.get_all():
            for movimentacao in operacao.movimentacao:
                if movimentacao.conta.codigo == conta.codigo:
                    data = operacao.data_operacao
                    tipo_operacao = operacao.tipo
                    if tipo_operacao == self.TIPOS_OPERACOES[1]:
                        dados_operacao = {"Codigo": movimentacao.conta.codigo, "Tipo": tipo_operacao.ljust(21), "Data": data.strftime("%b %d %Y %H:%M:%S"), "Valor": (movimentacao.valor * -1), "Chave": operacao.chave, "Desc": movimentacao.descricao}
                    elif tipo_operacao == self.TIPOS_OPERACOES[2]:
                        dados_operacao = {"Codigo": movimentacao.conta.codigo, "Tipo": tipo_operacao.ljust(21), "Data": data.strftime("%b %d %Y %H:%M:%S"), "Valor": movimentacao.valor, "Chave": operacao.chave, "Desc": movimentacao.descricao}
                    else:
                        if movimentacao.valor > 0:
                            dados_operacao = {"Codigo": movimentacao.conta.codigo, "Tipo": tipo_operacao,
                                          "Data": data.strftime("%b %d %Y %H:%M:%S"), "Valor": movimentacao.valor, "Chave": operacao.chave, "Desc": movimentacao.descricao}
                        else:
                            dados_operacao = {"Codigo": movimentacao.conta.codigo, "Tipo": tipo_operacao,
                                              "Data": data.strftime("%b %d %Y %H:%M:%S"), "Valor": (movimentacao.valor * -1),
                                              "Chave": operacao.chave, "Desc": movimentacao.descricao}
                    operacoes.append(dados_operacao)
        self.__tela_operacao.exibe_extrato(conta.saldo, operacoes)

    def consultar_saldo(self, conta, opcao_escolhida):
        saldo_final = conta.saldo
        saldo_depositos = 0
        saldo_saques = 0
        saldo_transferencia_enviadas = 0
        saldo_transferencia_recebidas = 0
        for operacao in self.__operacao_dao.get_all():
            for movimentacao in operacao.movimentacao:
                if movimentacao.conta.codigo == conta.codigo:
                    if operacao.tipo == self.TIPOS_OPERACOES[1]:
                        saldo_saques += (movimentacao.valor * -1)
                    elif operacao.tipo == self.TIPOS_OPERACOES[2]:
                        saldo_depositos += movimentacao.valor
                    else:
                        if movimentacao.valor < 0:
                            saldo_transferencia_enviadas += (movimentacao.valor * -1)
                        else:
                            saldo_transferencia_recebidas += movimentacao.valor
        saldo_transferencia_entrada_vs_saida = saldo_transferencia_recebidas + saldo_depositos - saldo_transferencia_enviadas - saldo_saques
        self.__tela_operacao.exibe_saldo(saldo_final, saldo_depositos, saldo_saques, saldo_transferencia_enviadas, saldo_transferencia_recebidas, saldo_transferencia_entrada_vs_saida)

    def abre_tela(self, conta):
        lista_opcoes = {1: self.saque, 2: self.deposito, 3: self.transferencia,
                        4: self.transferencia_PIX, 5: self.consultar_extrato, 6: self.consultar_saldo,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_operacao.exibe_menu_operacoes(conta.agencia, conta.codigo)
            self.__tela_operacao.close()
            if opcao_escolhida != None:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                if opcao_escolhida != 0:
                    funcao_escolhida(conta, opcao_escolhida)
                else:
                    funcao_escolhida()
            else:
                exit(0)
