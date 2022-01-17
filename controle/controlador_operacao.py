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

    #def verifica_opeeracao(valor)
    #   while(valor > conta.saldo or valor <= 0):
    #       print("Valor inválido, tente novamente")
    #       valor = int(input("Digite qual o valor da operação: "))
    #   return true

    #def saque(self):
    #   valor_saque = int(input("Digite qual valor deseja sacar: "))
    #   if(verifica_operacao(valor_saque)):
    #   #   saldo -= valor_saque
    #       extrato.append("Saque R$" + valor_saque)
    #       print("saque realizado com sucesso")

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

    #def verificar_extrato(self):
    #    for i in range(extrato):
    #       print(i)

    def abre_tela(self):
        lista_opcoes = {1: self.teste, 2: self.teste, 3: self.teste,
                        4: self.teste, 5: self.teste, 6: self.teste,
                        0: self.retorno_menu}

        while True:
            opcao_escolhida = self.__tela_operacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()