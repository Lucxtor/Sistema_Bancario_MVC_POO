from limite.tela_operacao import TelaOperacao
from datetime import datetime

class ControladorOperacao:

    def __init__(self, controlador_conta):
        self.__operacoes = []
        self.__tela_operacao = TelaOperacao()
        self.__controlador_conta = controlador_conta

    def retorno_menu(self):
        self.__controlador_conta.retorno_menu_principal()

    def teste(self):
        print("\nEscolheu uma opção diferente de retornar ao menu anterior\n")

    def saque(self, codigo_conta):
        dados_saque = self.__tela_operacao.pega_dados_saque()
    #       fazer semelhante ao deposito passando valor negativo para a função atualiza saldo
        self.__tela_operacao.mostra_mensagem("Operação realizada com sucesso")

    def deposito(self, codigo_conta):
        dados_deposito = {"conta": codigo_conta, "tipo_opercao": 2, "data": datetime.now(), "valor": self.__tela_operacao.pega_dados_deposito()}
        self.__controlador_conta.atualizar_saldo(dados_deposito["conta"], dados_deposito["valor"])
        self.__operacoes.append(dados_deposito)
        self.__tela_operacao.mostra_mensagem("Operação realizada com sucesso")

    #def transferencia(self):
    #   nome_transferencia = input("Digite o nome do favorecido")
    #   cpf_transferencia = input("Digite o CPF do favorecido")
    #   if(cpf_transferencia encontrado na lista de cpf):
    #       listar números e tipos de conta daquele cpf
    #       conta_transferencia = input("Digite qual das contas receberá a transferência")
    #       while(número inválido):
    #       print("número inválido, digite apenas ...")
    #       valor_transferencia = int(input("Digite qual valor deseja transferir: "))
    #       if(verifica_operacao(valor_transferencia)):
    #           saldo -= valor_transferencia
    #           saldo_favorecido += valor_transferencia
    #           extrato.append("Transferência R$" + valor_saque + " " + nome_transferência )
    #           print("transferência para " + nome_transferencia + " realizada com sucesso!")
    #   else():
    #       print("CPF não encontrado nos registros. Verifique os dados e tente novamente")

    def transferencia_PIX(self, codigo_conta):
        pass

    #def verificar_extrato(self):
    #    for i in range(extrato):
    #       print(i)

    def abre_tela(self, codigo_conta):
        lista_opcoes = {1: self.teste, 2: self.deposito, 3: self.teste,
                        4: self.teste, 5: self.teste, 6: self.teste,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_operacao.tela_opcoes(codigo_conta)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if opcao_escolhida != 0:
                funcao_escolhida(codigo_conta)
            else:
                funcao_escolhida()
